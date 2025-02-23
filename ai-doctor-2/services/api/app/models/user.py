from services.api.app.helper.db import get_db_connection
from services.api.app.helper.security import hash_password, verify_password, create_access_token
from fastapi import HTTPException

async def create_user(username: str, password: str):
    hashed_pw = hash_password(password)
    query = """
    INSERT INTO users (username, password)
    VALUES ($1, $2)
    RETURNING id;
    """
    conn = await get_db_connection()
    try:
        user_id = await conn.fetchval(query, username, hashed_pw)
        return {"user_id": user_id, "username": username}
    finally:
        await conn.close()

async def authenticate_user(username: str, password: str):
    query = "SELECT * FROM users WHERE username = $1"
    conn = await get_db_connection()
    try:
        user = await conn.fetchrow(query, username)
        if not user or not verify_password(password, user["password"]):
            raise HTTPException(status_code=400, detail="Invalid credentials")
        token = create_access_token({"sub": username})
        return {"access_token": token, "token_type": "bearer"}
    finally:
        await conn.close()


