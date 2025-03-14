from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from app.helper.security import check_role
from app.helper.db import database
import asyncpg

router = APIRouter()

@router.post("/card/register", dependencies=[Depends(check_role("register_patient"))])
async def register_patient(first_name: str, last_name: str, age: int, phone: Optional[str] = None):
    """
    Register a new patient in the system.
    - `first_name`: First name of the patient
    - `last_name`: Last name of the patient
    - `age`: Age of the patient
    - `phone`: Optional phone number
    """
    async with database.acquire() as conn:
        await conn.execute(
            "INSERT INTO patients (first_name, last_name, age, phone, status) VALUES ($1, $2, $3, $4, 'Pending')",
            first_name, last_name, age, phone
        )
    
    return {"message": "Patient successfully registered"}
