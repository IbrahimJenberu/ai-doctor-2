CREATE TABLE IF NOT EXISTS patient_status (
    id SERIAL PRIMARY KEY,
    patient_id INT NOT NULL REFERENCES patients(id) ON DELETE CASCADE,
    status VARCHAR(50) NOT NULL CHECK (status IN ('pending', 'assigned_to_opd', 'lab_requested', 'lab_completed', 'discharged')),
    updated_by INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    updated_at TIMESTAMP DEFAULT NOW()
);

