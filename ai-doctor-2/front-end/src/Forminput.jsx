import React from 'react'

function Forminput() {
  return (
    <div className='form-group mb-2 '>
    <label htmlFor={props.type} className='form-label'>{props.label}</label>
    <input type={props.type} className='form-control was-validated' required></input>
<div className='invalid-feedback'>{props.feedback}</div>
</div>
  )
}

export default Forminput