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

@router.get("/card/patients", dependencies=[Depends(check_role("view_patients"))])
async def filter_patients(patient_id: Optional[int] = None, name: Optional[str] = None):
    """
    Retrieve patient details by ID or name.
    If both parameters are provided, ID is prioritized.
    """
    query = "SELECT * FROM patients"
    params = []
    
    if patient_id:
        query += " WHERE id=$1"
        params.append(patient_id)
    elif name:
        query += " WHERE first_name ILIKE $1 OR last_name ILIKE $1"
        params.append(f"%{name}%")
    
    async with database.acquire() as conn:
        patients = await conn.fetch(query, *params) if params else await conn.fetch(query)
    
    return {"patients": [dict(p) for p in patients]}

@router.post("/card/assign_patient", dependencies=[Depends(check_role("assign_opd"))])
async def assign_patient_to_opd(patient_id: int):
    """
    Assign a patient to the OPD Room for medical examination.
    Ensures the patient exists before assignment.
    """
    async with database.acquire() as conn:
        patient = await conn.fetchrow("SELECT * FROM patients WHERE id=$1", patient_id)
        if not patient:
            raise HTTPException(status_code=404, detail="Patient not found")
        
        # Update patient status to 'Assigned to OPD'
        await conn.execute("UPDATE patients SET status='Assigned to OPD' WHERE id=$1", patient_id)
    
    return {"message": "Patient assigned to OPD successfully"}

@router.post("/card/schedule_appointment", dependencies=[Depends(check_role("schedule_appointment"))])
async def schedule_appointment(patient_id: int, doctor_id: int, date: str):
    """
    Schedule an appointment for a patient with a specific doctor.
    Ensures valid patient and doctor IDs before scheduling.
    """
    async with database.acquire() as conn:
        patient = await conn.fetchrow("SELECT id FROM patients WHERE id=$1", patient_id)
        doctor = await conn.fetchrow("SELECT id FROM doctors WHERE id=$1", doctor_id)
        if not patient:
            raise HTTPException(status_code=404, detail="Patient not found")
        if not doctor:
            raise HTTPException(status_code=404, detail="Doctor not found")
        
        # Insert appointment into the database
        await conn.execute(
            "INSERT INTO appointments (patient_id, doctor_id, date, status) VALUES ($1, $2, $3, 'Scheduled')",
            patient_id, doctor_id, date
        )
    
    return {"message": "Appointment scheduled successfully"}

