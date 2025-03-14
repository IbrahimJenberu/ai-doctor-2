# services/api/app/router/opd.py

from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.helper.security import check_role
from app.helper.db import database
import asyncpg

router = APIRouter(prefix="/opd", tags=["OPD"])

# View Assigned Patients
@router.get("/assigned_patients", dependencies=[Depends(check_role("read_patients"))])
async def view_assigned_patients():
    """Retrieve patients assigned to the OPD room from Card Room notifications."""
    async with database.acquire() as conn:
        patients = await conn.fetch("SELECT * FROM patients WHERE status='Assigned to OPD'")
    return {"assigned_patients": [dict(p) for p in patients]}

# View & Manage Patient History
@router.get("/patient_history/{patient_id}", dependencies=[Depends(check_role("view_medical_records"))])
async def view_patient_history(patient_id: int):
    """Retrieve a patient's full medical history."""
    async with database.acquire() as conn:
        history = await conn.fetch("SELECT * FROM medical_history WHERE patient_id=$1", patient_id)
    if not history:
        raise HTTPException(status_code=404, detail="No history found")
    return {"patient_history": [dict(h) for h in history]}

@router.post("/update_history", dependencies=[Depends(check_role("write_prescriptions"))])
async def update_patient_history(patient_id: int, notes: str):
    """Update patient history with new notes or diagnoses."""
    async with database.acquire() as conn:
        await conn.execute(
            "INSERT INTO medical_history (patient_id, notes) VALUES ($1, $2)", patient_id, notes
        )
    return {"message": "Patient history updated"}

# AI-Based Analysis: Symptom, MRI, and Chest X-ray
@router.post("/analyze_symptoms", dependencies=[Depends(check_role("analyze_symptoms"))])
async def analyze_symptoms(patient_id: int, symptoms: List[str]):
    """Send symptoms to AI Symptom Analyzer and return a prediction."""
    # Call AI model microservice (simulated response)
    prediction = {"diagnosis": "Possible Pneumonia", "probability": 85.3}
    return {"patient_id": patient_id, "analysis": prediction}

@router.post("/analyze_brain_mri", dependencies=[Depends(check_role("analyze_mri"))])
async def analyze_brain_mri(patient_id: int, image_url: str):
    """Send Brain MRI to AI Analyzer and return the ranked disease probabilities."""
    # Call AI model microservice (simulated response)
    result = {"top_diagnoses": ["Glioblastoma", "Meningioma"], "probabilities": [70, 30]}
    return {"patient_id": patient_id, "mri_analysis": result}
