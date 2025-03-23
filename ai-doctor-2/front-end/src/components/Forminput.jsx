import React from 'react';

function Forminput({ type, label, feedback }) {
  return (
    <div className="form-group mb-2">
      <label htmlFor={type} className="form-label">{label}</label>
      <input type={type} id={type} className="form-control was-validated" required />
      <div className="invalid-feedback">{feedback}</div>
    </div>
  );
}

export default Forminput;
