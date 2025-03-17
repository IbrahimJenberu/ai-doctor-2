from typing import Dict, Any, List
from asyncpg import Pool

# Authentication Queries
REGISTER_USER = "INSERT INTO users (username, hashed_password, role) VALUES ($1, $2, $3) RETURNING id"
GET_USER_BY_USERNAME = "SELECT * FROM users WHERE username = $1"

# Patient Queries
REGISTER_PATIENT = "INSERT INTO patients (first_name, last_name, dob, gender, contact_info) VALUES ($1, $2, $3, $4, $5) RETURNING id"
GET_PATIENT_BY_ID = "SELECT * FROM patients WHERE id = $1"
GET_ALL_PATIENTS = "SELECT * FROM patients"

# Appointment Queries
SCHEDULE_APPOINTMENT = """
    INSERT INTO appointments (patient_id, doctor_id, appointment_date)
    VALUES ($1, $2, $3) RETURNING id
"""
GET_APPOINTMENTS_BY_DOCTOR = "SELECT * FROM appointments WHERE doctor_id = $1"

# OPD Queries
GET_PATIENT_HISTORY = "SELECT * FROM opd_history WHERE patient_id = $1"
UPDATE_PATIENT_HISTORY = """
    INSERT INTO opd_history (patient_id, doctor_id, medical_history)
    VALUES ($1, $2, $3) RETURNING id
"""

# AI Analysis Queries
INSERT_AI_ANALYSIS = """
    INSERT INTO ai_analysis (patient_id, analysis_type, result) 
    VALUES ($1, $2, $3) RETURNING id
"""

# Lab Queries
GET_LAB_REQUESTS = "SELECT * FROM lab_requests WHERE status = 'Pending'"
INSERT_LAB_RESULT = """
    INSERT INTO lab_results (patient_id, lab_request_id, result) 
    VALUES ($1, $2, $3) RETURNING id
"""

class NotificationQueries:
    def __init__(self, db_pool: Pool):
        self.db_pool = db_pool

    async def create_notification(self, patient_id: int, user_id: int, message: Dict[str, Any], type: str):
        query = """
        INSERT INTO notifications (patient_id, user_id, message, type)
        VALUES ($1, $2, $3::jsonb, $4) RETURNING id, patient_id, user_id, message, type, status, created_at;
        """
        async with self.db_pool.acquire() as conn:
            return await conn.fetchrow(query, patient_id, user_id, message, type)

    async def get_notifications(self, user_id: int) -> List[Dict[str, Any]]:
        query = "SELECT * FROM notifications WHERE user_id = $1 ORDER BY created_at DESC;"
        async with self.db_pool.acquire() as conn:
            return await conn.fetch(query, user_id)

    async def mark_as_read(self, notification_id: int):
        query = "UPDATE notifications SET status = 'read', read_at = NOW() WHERE id = $1 RETURNING *;"
        async with self.db_pool.acquire() as conn:
            return await conn.fetchrow(query, notification_id)

class PatientStatusQueries:
    def __init__(self, db_pool: Pool):
        self.db_pool = db_pool

    async def update_status(self, patient_id: int, status: str, updated_by: int):
        query = """
        INSERT INTO patient_status (patient_id, status, updated_by)
        VALUES ($1, $2, $3) RETURNING id, patient_id, status, updated_by, updated_at;
        """
        async with self.db_pool.acquire() as conn:
            return await conn.fetchrow(query, patient_id, status, updated_by)

    async def get_status(self, patient_id: int):
        query = "SELECT * FROM patient_status WHERE patient_id = $1 ORDER BY updated_at DESC LIMIT 1;"
        async with self.db_pool.acquire() as conn:
            return await conn.fetchrow(query, patient_id)
