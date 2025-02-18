// ADPPM/frontend/src/services/api.js
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000',  // Update with your FastAPI URL
});

export const registerPatient = async (patientData) => {
  return await api.post('/opd/register', patientData);
};
export const getPatientData = async (patientId) => {
  return await api.get(`/opd/patient/${patientId}`);
};