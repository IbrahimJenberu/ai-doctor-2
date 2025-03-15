import asyncpg
import os
from dotenv import load_dotenv
from contextlib import asynccontextmanager

# Load environment variables from .env file
load_dotenv()
DATABASE_URL = os.getenv("postgresql://ai_doctor_user:securepassword@localhost/ai_doctor_db")

class Database:
    """
    Database connection pool manager using asyncpg for high-performance async queries.
    - Uses connection pooling to optimize database interactions.
    - Ensures efficient queries with minimal latency.
    """
    pool = None

    @classmethod
    async def connect(cls):
        """Establish a connection pool to PostgreSQL."""
        if cls.pool is None:
            cls.pool = await asyncpg.create_pool(DATABASE_URL, min_size=2, max_size=10)


    @classmethod
    async def disconnect(cls):
        """Close the connection pool."""
        if cls.pool:
            await cls.pool.close()
            cls.pool = None

    @classmethod
    async def fetch(cls, query: str, *args):
        """Execute a SELECT query and return the results as a list of dictionaries."""
        async with cls.pool.acquire() as conn:
            rows = await conn.fetch(query, *args)
            return [dict(row) for row in rows]

    @classmethod
    async def fetch_one(cls, query: str, *args):
        """Execute a SELECT query and return a single row as a dictionary."""
        async with cls.pool.acquire() as conn:
            row = await conn.fetchrow(query, *args)
            return dict(row) if row else None

    @classmethod
    async def execute(cls, query: str, *args):
        """Execute an INSERT, UPDATE, or DELETE query and return the status."""
        async with cls.pool.acquire() as conn:
            return await conn.execute(query, *args)

@asynccontextmanager
async def lifespan(app):
    """Manage database connection lifecycle in FastAPI."""
    await Database.connect()
    yield
    await Database.disconnect()


