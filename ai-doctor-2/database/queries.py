from database.connection import Database

async def get_patient_by_id(patient_id: int):
    query = "SELECT * FROM patients WHERE id = $1"
    return await Database.fetch_one(query, patient_id)

async def create_patient(first_name: str, last_name: str, dob: str, gender: str, phone: str, email: str):
    query = """
    INSERT INTO patients (first_name, last_name, dob, gender, phone, email)
    VALUES ($1, $2, $3, $4, $5, $6) RETURNING id
    """
    return await Database.execute(query, first_name, last_name, dob, gender, phone, email)

async def get_appointments_by_doctor(doctor_id: int):
    query = "SELECT * FROM appointments WHERE doctor_id = $1 ORDER BY appointment_date"
    return await Database.fetch_all(query, doctor_id)

async def get_appointments_by_patient(patient_id: int):
    query = "SELECT * FROM appointments WHERE patient_id = $1 ORDER BY appointment_date"
    return await Database.fetch_all(query, patient_id)
