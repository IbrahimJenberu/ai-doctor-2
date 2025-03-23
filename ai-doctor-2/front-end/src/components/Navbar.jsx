import React from 'react';
import { NavLink, useNavigate } from 'react-router-dom';
import './Navbar.css';
import Gradientbtn from './Gradientbtn';

const Navbar = () => {
  const navigate = useNavigate();

  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-white shadow-sm">
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
              <NavLink to="/" className="nav-link">
                Home
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink to="/About" className="nav-link">
                About
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink to="/Services" className="nav-link">
                Services
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink to="/Contact" className="nav-link">
                Contacts
              </NavLink>
            </li>
          </ul>
          <div className="d-flex align-items-center Login">
            <button
              onClick={() => navigate('/Login')}
              className="d-lg-inline btn btn-primary px-4 py-2 rounded-pill fw-semibold"
            >
              LOGIN
            </button>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
