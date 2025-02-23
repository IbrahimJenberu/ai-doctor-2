from fastapi import APIRouter, Depends, HTTPException
from services.api.app.models.user import create_user, authenticate_user
from services.api.app.schema.user import UserCreate, UserLogin

router = APIRouter()

@router.get("/auth")
async def get_auth_data():
    return {"message": "Auth data"}

@router.post("/register/")
async def register_user(user: UserCreate):
    return await create_user(user.username, user.password)

@router.post("/login/")
async def login_user(user: UserLogin):
    return await authenticate_user(user.username, user.password)
