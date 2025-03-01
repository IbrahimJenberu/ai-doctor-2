import asyncpg
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://auth_user:admin123@pgdb:5432/ai_doctor_db")

class Database:
    _pool = None

    @classmethod
    async def connect(cls):
        if cls._pool is None:
            cls._pool = await asyncpg.create_pool(DATABASE_URL, min_size=1, max_size=5)
        return cls._pool

    @classmethod
    async def disconnect(cls):
        if cls._pool:
            await cls._pool.close()
            cls._pool = None

    @classmethod
    async def fetch_one(cls, query, *args):
        async with cls._pool.acquire() as conn:
            return await conn.fetchrow(query, *args)

    @classmethod
    async def fetch_all(cls, query, *args):
        async with cls._pool.acquire() as conn:
            return await conn.fetch(query, *args)

    @classmethod
    async def execute(cls, query, *args):
        async with cls._pool.acquire() as conn:
            return await conn.execute(query, *args)

