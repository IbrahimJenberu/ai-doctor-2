from database.connection import Database

async def initialize_database():
    pool = await Database.connect()
    async with pool.acquire() as conn:
        await conn.execute(open("database/migrations/001_init.sql").read())
        await conn.execute(open("database/migrations/002_add_indexes.sql").read())
    await pool.close()

async def reset_database():
    pool = await Database.connect()
    async with pool.acquire() as conn:
        await conn.execute("DROP SCHEMA public CASCADE; CREATE SCHEMA public;")
        await initialize_database()
    await pool.close()

