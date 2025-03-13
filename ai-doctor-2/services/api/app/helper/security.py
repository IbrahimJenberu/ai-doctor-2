# services/api/app/helper/security.py

from fastapi import HTTPException, Depends
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
import os
from dotenv import load_dotenv

load_dotenv()

# Password hashing setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 setup
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# JWT Secret & Algorithm
SECRET_KEY = os.getenv("JWT_SECRET", "admin123")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# Define User Roles
ROLES = {
    "doctor": ["read_patients", "write_prescriptions", "view_medical_records"],
    "lab_technician": ["process_tests", "view_lab_results"],
    "card_worker": ["register_patient", "manage_appointments"]
}


def hash_password(password: str) -> str:
    """Hashes a password for secure storage."""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifies a given password against the stored hashed password."""
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Generates a JWT access token."""
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta if expires_delta else timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str):
    """Decodes and verifies a JWT token."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None


def get_current_user(token: str = Depends(oauth2_scheme)):
    """Extracts the current user from the JWT token."""
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid authentication token")
    return payload


def check_role(required_role: str):
    """Middleware function to check user role before accessing certain routes."""
    def role_checker(payload: dict = Depends(get_current_user)):
        user_role = payload.get("role")
        if user_role not in ROLES or required_role not in ROLES[user_role]:
            raise HTTPException(status_code=403, detail="Insufficient permissions")
        return payload
    return role_checker
