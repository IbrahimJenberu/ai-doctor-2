# services/api/app/router/auth.py

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from datetime import timedelta
from app.helper.security import (
    hash_password, verify_password, create_access_token, get_current_user
)
from app.helper.db import database  # Assuming `database.py` handles asyncpg connection
import asyncpg

router = APIRouter(prefix="/auth", tags=["Authentication"])


class UserRegister(BaseModel):
    username: str
    password: str
    role: str  # Role must be "doctor", "lab_technician", or "card_worker"


class UserLogin(BaseModel):
    username: str
    password: str


@router.post("/register")
async def register_user(user: UserRegister):
    """Registers a new user with role-based access control."""
    if user.role not in ["doctor", "lab_technician", "card_worker"]:
        raise HTTPException(status_code=400, detail="Invalid role specified")

    hashed_password = hash_password(user.password)
    try:
        async with database.acquire() as conn:
            await conn.execute(
                "INSERT INTO users (username, password, role) VALUES ($1, $2, $3)",
                user.username, hashed_password, user.role
            )
    except asyncpg.UniqueViolationError:
        raise HTTPException(status_code=400, detail="Username already exists")

    return {"message": "User registered successfully"}


@router.post("/login")
async def login(user: UserLogin):
    """Authenticates a user and returns a JWT token."""
    async with database.acquire() as conn:
        row = await conn.fetchrow("SELECT username, password, role FROM users WHERE username=$1", user.username)

    if not row or not verify_password(user.password, row["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token({"sub": row["username"], "role": row["role"]}, timedelta(hours=1))
    return {"access_token": access_token, "token_type": "bearer"}
