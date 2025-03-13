import os
import jwt
import bcrypt
import datetime
from dotenv import load_dotenv
from fastapi import HTTPException, Security, Depends
from fastapi.security import OAuth2PasswordBearer

# Load environment variables
load_dotenv()

# Secret key & Algorithm
SECRET_KEY = os.getenv("SECRET_KEY", "admin123")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

def hash_password(password: str) -> str:
    """
    Hashes a password using bcrypt.
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies if the provided password matches the stored hash.
    """
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def create_access_token(data: dict, expires_delta: int = ACCESS_TOKEN_EXPIRE_MINUTES):
    """
    Generates a JWT access token with an expiration time.
    """
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=expires_delta)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_access_token(token: str):
    """
    Decodes and verifies a JWT access token.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

def get_current_user(token: str = Security(oauth2_scheme)):
    """
    Retrieves user information from the JWT token.
    """
    payload = verify_access_token(token)
    return payload
