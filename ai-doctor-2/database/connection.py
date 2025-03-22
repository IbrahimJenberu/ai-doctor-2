import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://auth_user:admin123@pgdb:5432/ai_doctor_db")

class Database:
    """Manages PostgreSQL database connection with asyncpg"""
    
    def __init__(self):
        self.pool = None

    async def connect(self):
        """Initialize connection pool"""
        self.pool = await asyncpg.create_pool(DATABASE_URL, min_size=5, max_size=20)

    async def disconnect(self):
        """Close connection pool"""
        if self.pool:
            await self.pool.close()

    async def fetch_one(self, query, *args):
        """Fetch a single record"""
        async with self.pool.acquire() as conn:
            return await conn.fetchrow(query, *args)

    async def fetch_all(self, query, *args):
        """Fetch multiple records"""
        async with self.pool.acquire() as conn:
            return await conn.fetch(query, *args)

    async def execute(self, query, *args):
        """Execute query (INSERT, UPDATE, DELETE)"""
        async with self.pool.acquire() as conn:
            return await conn.execute(query, *args)

db = Database()
