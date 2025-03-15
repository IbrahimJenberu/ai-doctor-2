from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import asyncpg
import jwt
import datetime
from passlib.context import CryptContext
from app.helper.db import database
from dotenv import load_dotenv

# Router for authentication endpoints
router = APIRouter(prefix="/auth", tags=["Authentication"])

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 password scheme for token-based authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# JWT Secret Key & Algorithm
SECRET_KEY = load_dotenv.JWT_SECRET_KEY  # Load from .env file
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # 1 hour
