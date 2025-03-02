from fastapi import APIRouter, Depends, HTTPException
from services.api.app.models.patient import create_patient, get_patient
from services.api.app.schema.patient import PatientCreate
from services.api.app.gateway.auth import get_current_user

router = APIRouter()

@router.get("/card")
async def get_card_info():
    # Implement the logic to retrieve card room information
    return {"message": "Card Room info"}

@router.post("/patients/")
async def add_patient(patient: PatientCreate):
    # Implement the logic to create patient information
    return await create_patient(patient.first_name, patient.last_name, patient.dob, patient.gender)

@router.get("/patients/{patient_id}")
async def fetch_patient(patient_id: int):
    patient = await get_patient(patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return dict(patient)
