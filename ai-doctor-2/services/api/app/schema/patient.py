# ADPPM/services/api/app/schema/patient.py

from pydantic import BaseModel

class PatientCreate(BaseModel):
    first_name: str
    last_name: str
    dob: str
    gender: str
    phone_number: str

class Patient(BaseModel):
    id: int
    first_name: str
    last_name: str
    dob: str
    gender: str
    phone_number: str
