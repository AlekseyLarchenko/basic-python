"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
from jsonplaceholder_requests import get_user_data, get_posts_data
from models import Base, Session, User, Post, engine


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def add_users(users_data):
    async with Session() as session:
        for user_data in users_data:
            user = User(name=user_data['name'], username=user_data['username'], email=user_data['email'])
            session.add(user)



async def add_posts(posts_data):
    async with Session() as session:
        for post_data in posts_data:
            post = Post(user_id=post_data['userId'], title=post_data['title'], body=post_data['body'])
            session.add(post)


async def async_main():
    await create_tables()


    users_data, posts_data = await asyncio.gather(
        get_user_data(),
        get_posts_data(),
    )

    await asyncio.gather(
        add_users(users_data),
        add_posts(posts_data),
    )

    await engine.dispose()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()