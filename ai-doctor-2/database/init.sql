-- Ensure the database and user are created
CREATE DATABASE ai_doctor_db;
CREATE USER ai_doctor_user WITH ENCRYPTED PASSWORD 'securepassword';
GRANT ALL PRIVILEGES ON DATABASE ai_doctor_db TO ai_doctor_user;

-- Create the patients table
CREATE TABLE IF NOT EXISTS patients (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    dob DATE,
    gender VARCHAR(10),
    phone_number VARCHAR(15)
);
