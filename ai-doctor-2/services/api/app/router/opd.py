from fastapi import APIRouter

from app.schema import patient as schema
router = APIRouter()

@router.get("/opd")
async def get_opd_data():
    return {"message": "OPD data"}

@router.post("/register")
async def register_patient(patient: schema.PatientCreate):
    # Here we would call the database and add a patient record
    return {"message": "Patient registered", "patient": patient}
