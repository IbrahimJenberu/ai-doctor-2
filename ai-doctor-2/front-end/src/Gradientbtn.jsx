import React from 'react'
import './Gradientbtn.css'
function Gradientbtn( {text, onClick, className }) {
  return (
    <button 
    onClick={onClick}
    className={`Gradientbtn btn btn-primary px-4 py-2 rounded-pill fw-semibold  ${className}`}
> 
    { <a href="./Login.jsx" className='link' >{text}  </a> }
  </button>
  )
}

export default Gradientbtn


