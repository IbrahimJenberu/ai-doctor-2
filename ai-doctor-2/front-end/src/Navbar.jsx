import React from 'react';
import Gradientbtn from './Gradientbtn';
import './Navbar.css';

function Navbar() {
  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-white fixed-top shadow-sm">
      <div className="container">
        <a className="navbar-brand text-primary fw-bold" href="#">
          ProDocAI
        </a>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav mx-auto">
            <li className="nav-item">
              <a className="nav-link" href="index.html">
                Home
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="About.html">
                About
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="Services.html">
                Services
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="Contact.html">
                Contact
              </a>
            </li>
          </ul>
        <div className="d-flex align-items-center">
          <Gradientbtn text="LOGIN" className=" d-lg-inline" />
        </div>
        </div>

      </div>
    </nav>
  );
}

export default Navbar;
