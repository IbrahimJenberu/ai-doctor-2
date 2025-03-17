from database.connection import Database

async def get_user_by_username(username: str):
    """Retrieve user by username."""
    query = "SELECT * FROM users WHERE username = $1"
    return await Database.fetchrow(query, username)

async def register_patient(first_name: str, last_name: str, dob: str, gender: str, contact: str):
    """Register a new patient."""
    query = """
        INSERT INTO patients (first_name, last_name, dob, gender, contact_info) 
        VALUES ($1, $2, $3, $4, $5) RETURNING id
    """
    return await Database.fetchrow(query, first_name, last_name, dob, gender, contact)

async def schedule_appointment(patient_id: str, doctor_id: str, date: str):
    """Schedule a new appointment."""
    query = """
        INSERT INTO appointments (patient_id, doctor_id, appointment_date) 
        VALUES ($1, $2, $3) RETURNING id
    """
    return await Database.fetchrow(query, patient_id, doctor_id, date)

async def get_appointments_by_doctor(doctor_id: str):
    """Retrieve appointments by doctor."""
    query = "SELECT * FROM appointments WHERE doctor_id = $1"
    return await Database.fetch(query, doctor_id)
