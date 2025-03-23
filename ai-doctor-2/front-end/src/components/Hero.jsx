import React from 'react'

import './Hero.css'
function Hero() {
  return (
    <section className=" hero vh-100  d-flex align-items-center position-relative text-white text-start " >
    <div className="position-absolute top-0 start-0 w-100 h-100  hero"></div>
    <div className="container position-relative z-2">
      <p className="fs-5">We are with you!</p>
      <h2 className="display-4 fw-bold">Professional Doctors to protect you</h2>
      <p className="fs-6">thats why we are the best here in this industry With AI Empowered </p>
      <button
     
              className="d-lg-inline btn btn-primary px-4 py-2 rounded-pill fw-semibold"
            >
              START NOW
            </button>
    </div>
  </section>
  )
}

export default Hero