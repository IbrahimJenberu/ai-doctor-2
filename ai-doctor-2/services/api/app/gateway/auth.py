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


# Utility Function: Hash Password
async def hash_password(password: str) -> str:
    return pwd_context.hash(password)


# Utility Function: Verify Password
async def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# Utility Function: Generate JWT Token
async def create_access_token(data: dict, expires_delta: int = ACCESS_TOKEN_EXPIRE_MINUTES):
    """Generate a JWT token."""
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=expires_delta)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# User Login & Token Generation
@router.post("/login")
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    """Authenticate user and return JWT token."""
    query = "SELECT user_id, username, password, role FROM users WHERE username=$1"
    
    async with database.acquire() as conn:
        user = await conn.fetchrow(query, form_data.username)

    if not user or not await verify_password(form_data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Generate access token
    token_data = {"sub": user["username"], "role": user["role"], "user_id": user["user_id"]}
    access_token = await create_access_token(token_data)

    return {"access_token": access_token, "token_type": "bearer"}


# Get Current User from Token
async def get_current_user(token: str = Depends(oauth2_scheme)):
    """Decode JWT and return the authenticated user."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        role: str = payload.get("role")
        user_id: int = payload.get("user_id")

        if username is None or role is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        return {"username": username, "role": role, "user_id": user_id}

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")



# Role-Based Authorization
async def get_current_active_user(current_user: dict = Depends(get_current_user)):
    """Ensures user is authenticated and active."""
    return current_user


async def get_admin_user(current_user: dict = Depends(get_current_user)):
    """Ensures the user has an 'admin' role."""
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    return current_user

