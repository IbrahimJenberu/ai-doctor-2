import React from 'react'
import Gradientbtn from './Gradientbtn'
import './Hero.css'
function Hero() {
  return (
    <section className=" hero vh-100  d-flex align-items-center position-relative text-white text-start " >
    <div className="position-absolute top-0 start-0 w-100 h-100 bg-primary opacity-50"></div>
    <div className="container position-relative z-2">
      <p className="fs-5">We are with you!</p>
      <h2 className="display-4 fw-bold">Professional Doctors to protect you</h2>
      <p className="fs-6">thats why we are the best here in this industry With AI Empowered </p>
      <Gradientbtn text="START NOW" />
    </div>
  </section>
  )
}

export default Hero