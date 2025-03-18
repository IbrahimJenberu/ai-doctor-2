CREATE TABLE IF NOT EXISTS notifications (
    id SERIAL PRIMARY KEY,
    patient_id INT NOT NULL REFERENCES patients(id) ON DELETE CASCADE,
    user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE, -- Doctor or Lab Technician
    message JSONB NOT NULL, -- Structured notification data
    type VARCHAR(50) NOT NULL CHECK (type IN ('patient_assigned', 'lab_request', 'lab_result')),
    status VARCHAR(20) DEFAULT 'unread' CHECK (status IN ('unread', 'read')),
    created_at TIMESTAMP DEFAULT NOW(),
    read_at TIMESTAMP NULL
);
