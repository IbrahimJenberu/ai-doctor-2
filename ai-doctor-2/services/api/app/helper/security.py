from typing import List
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import BaseModel
from helper.auth_helper import verify_token
from helper.db import fetch_user_by_id

# OAuth2 scheme for token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Define roles
ROLES = {
    "doctor": ["view_patients", "request_lab", "analyze_ai_results"],
    "lab_technician": ["process_lab_tests", "upload_results"],
    "card_room_worker": ["register_patient", "update_status", "assign_doctor"]
}

class TokenData(BaseModel):
    user_id: str
    role: str

def get_current_user(token: str = Depends(oauth2_scheme)):
    """Decode and verify JWT token, then return user info."""
    try:
        payload = verify_token(token)
        user_id: str = payload.get("sub")
        role: str = payload.get("role")
        if not user_id or not role:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        return TokenData(user_id=user_id, role=role)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

def check_role(required_permissions: List[str]):
    """Dependency to enforce role-based access control (RBAC)."""
    def role_dependency(user: TokenData = Depends(get_current_user)):
        user_permissions = ROLES.get(user.role, [])
        if not any(permission in user_permissions for permission in required_permissions):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
        return user
    return role_dependency
