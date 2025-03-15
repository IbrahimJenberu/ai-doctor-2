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
