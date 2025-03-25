import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Contact.css'
const Contactpage = () => {
  return (
    <div className="container py-5">
      <div className="row justify-content-center align-items-center">
        {/* Left Section */}
        <div className="col-md-6 text-start">
          <h5 className="text-dark fw-semibold">Doctor Appointment</h5>
          <h2 className="fw-bold mt-2">Book your appointment for a doctor</h2>
          <p className="text-muted mt-4">
            Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est la unde omnis iste natus
          </p>
          <h3 className="mt-4 fw-semibold">Or call this number</h3>
          <p className="text-primary fs-4 fw-bold">+880 1234 567 890</p>
        </div>
        
        {/* Right Section (Form) */}
        <div className="contact-form col-md-5 p-5  text-white rounded shadow-lg" style={{ minHeight: '550px' }}>
          <h3 className="fw-semibold mb-3">Please fill this form</h3>
          <form>
            <div className="mb-3">
              <input type='text' placeholder='Your Name' required className="form-control"/>
            </div>
            <div className='row mb-3'>
              <div className="col">
                <input type="email" placeholder="Your Email" required className="form-control"/>
              </div>
              <div className="col">
                <input type="text" placeholder="Phone No" required className="form-control"/>
              </div>
            </div>
            <div className="mb-3">
              <select required className="form-select"> 
                <option value="" disabled selected>Select A Department</option>
                <option value="medicine">Medicine</option>
                <option value="dental">Dental</option>
                <option value="cardiology">Cardiology</option>
              </select>
            </div>
            <div className="mb-3">
              <select required className="form-select">
                <option value="" disabled selected>Select A Doctor</option>
                <option value="dr-smith">Dr. Smith</option>
                <option value="dr-jane">Dr. Jane</option>
                <option value="dr-john">Dr. John</option>
              </select>
            </div>
            <div className='row mb-3'>
              <div className="col">
                <input type='date' required className="form-control"/>
              </div>
              <div className="col">
                <input type='time' required className="form-control"/>
              </div>
            </div>
            <div className="mb-3">
              <textarea placeholder='Write down the problem' className="form-control"></textarea>
            </div>
            <button type='submit' className="btn btn-light w-100 fw-semibold">Book An Appointment</button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Contactpage;
