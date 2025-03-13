import datetime
import asyncpg
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

async def init_db():
    """
    Initializes the PostgreSQL database and creates the notifications table if it doesn't exist.
    """
    conn = await asyncpg.connect(DATABASE_URL)
    await conn.execute("""
        CREATE TABLE IF NOT EXISTS notifications (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            event_type TEXT NOT NULL,
            event_data TEXT NOT NULL,
            timestamp TIMESTAMP DEFAULT now()
        );
    """)
    await conn.close()
