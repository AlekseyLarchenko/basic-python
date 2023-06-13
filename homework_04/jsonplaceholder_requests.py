"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
from aiohttp import ClientSession

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(session, url):
    async with session.get(url) as response:
        return await response.json()


async def get_posts_data():
    async with ClientSession() as session:
        posts_data = await fetch_json(session, POSTS_DATA_URL)
        return posts_data


async def get_user_data():
    async with ClientSession() as session:
        users_data = await fetch_json(session, USERS_DATA_URL)
        print(users_data)
