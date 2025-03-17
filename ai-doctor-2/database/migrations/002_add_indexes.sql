-- Speed up lookups on common queries
CREATE INDEX idx_users_role ON users(role);
CREATE INDEX idx_patients_dob ON patients(dob);
CREATE INDEX idx_appointments_patient_id ON appointments(patient_id);
CREATE INDEX idx_opd_history_patient_id ON opd_history(patient_id);
CREATE INDEX idx_lab_requests_patient_id ON lab_requests(patient_id);
CREATE INDEX idx_ai_analysis_patient_id ON ai_analysis(patient_id);
CREATE INDEX idx_lab_results_patient_id ON lab_results(patient_id);
