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
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from jsonplaceholder_requests import get_user_data, get_posts_data
from models import Base, User, Post

PG_CONN_URI = "postgresql+asyncpg://username:passwd@0.0.0.0:5433/blog"

Engine = create_engine(PG_CONN_URI)
Session = sessionmaker(
    Engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def add_users_data():
    session = Session()
    users_data = await get_user_data()
    users = [User(name=user['name'], username=user['username'], email=user['email']) for user in users_data]
    session.add_all(users)
    session.commit()
    session.close()


async def add_posts_data():
    session = Session()
    posts_data = await get_posts_data()
    posts = [Post(user_id=post['userId'], title=post['title'], body=post['body']) for post in posts_data]
    session.add_all(posts)
    session.commit()
    session.close()


async def async_main():
    Base.metadata.create_all(Engine)
    await asyncio.gather(add_users_data(), add_posts_data())
    Engine.dispose()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
