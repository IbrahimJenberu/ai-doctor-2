-- Enable UUID extension for unique identifiers
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Users Table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    username TEXT UNIQUE NOT NULL,
    hashed_password TEXT NOT NULL,
    role TEXT CHECK (role IN ('card_room', 'doctor', 'lab_technician')) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Patients Table
CREATE TABLE patients (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    dob DATE NOT NULL,
    gender TEXT CHECK (gender IN ('Male', 'Female', 'Other')) NOT NULL,
    contact_info TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Appointments Table
CREATE TABLE appointments (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    patient_id UUID REFERENCES patients(id) ON DELETE CASCADE,
    doctor_id UUID REFERENCES users(id) ON DELETE SET NULL,
    appointment_date TIMESTAMP NOT NULL,
    status TEXT CHECK (status IN ('Scheduled', 'Completed', 'Cancelled')) DEFAULT 'Scheduled',
    created_at TIMESTAMP DEFAULT NOW()
);

-- OPD History Table
CREATE TABLE opd_history (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    patient_id UUID REFERENCES patients(id) ON DELETE CASCADE,
    doctor_id UUID REFERENCES users(id) ON DELETE SET NULL,
    medical_history TEXT NOT NULL,
    updated_at TIMESTAMP DEFAULT NOW()
);

-- AI Analysis Table
CREATE TABLE ai_analysis (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    patient_id UUID REFERENCES patients(id) ON DELETE CASCADE,
    analysis_type TEXT CHECK (analysis_type IN ('Symptoms', 'Brain_MRI', 'Chest_XRay')) NOT NULL,
    result JSONB NOT NULL,
    analyzed_at TIMESTAMP DEFAULT NOW()
);

-- Lab Requests Table
CREATE TABLE lab_requests (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    patient_id UUID REFERENCES patients(id) ON DELETE CASCADE,
    requested_by UUID REFERENCES users(id) ON DELETE SET NULL,
    test_type TEXT NOT NULL,
    status TEXT CHECK (status IN ('Pending', 'Completed')) DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT NOW()
);

-- Lab Results Table
CREATE TABLE lab_results (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    patient_id UUID REFERENCES patients(id) ON DELETE CASCADE,
    lab_request_id UUID REFERENCES lab_requests(id) ON DELETE CASCADE,
    result JSONB NOT NULL,
    processed_at TIMESTAMP DEFAULT NOW()
);
