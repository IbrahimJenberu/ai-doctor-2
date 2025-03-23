import React from 'react'
import './Login.css'
import Forminput from '../components/Forminput'
import { useNavigate } from 'react-router-dom'
function Login() {
  const navigate=useNavigate();
  return (

<>  
<nav class="navbar " >
  <div class="container">

  <i class="fa fa-home"  onClick={()=>navigate('/')}></i> 

  </div>
</nav>

<div className='loginpage wrapper d-flex align-items-center justify-content-center w-200'> 
   <div className='login rounded'>
   
   <div class="toplogin">
    <div class="row px-3 pt-1">
    <div class="col-md-8 mt-2">
        <h3>Welcome!</h3>
        <p>sign in to continue browsing.</p>
    </div>
    <div  class="col-md-4 ">
    <img src="src/assets/headerlogo.png" alt="Vector Graphic" class="img-fluid"></img> 
    </div>
    </div>
</div>
      <div class="lowerlogin">

<form className='needs-validation'>
<div class="alert alert-danger" role="alert">
            Failed to fetch
</div>

<Forminput type="email" label="Email Address" feedback="Please Enter your Email" />
<Forminput type="password" label="Password" feedback="Please Enter your password" />

<div className='form-group mt-3'>
    <input type='checkbox'></input> 
    <label htmlFor='check'>  Remember me</label>
</div>
<button type='submit' className='btn  w-100 btn-success mt-4 mb-3 p-1 fs-6 '>Log in</button>

</form>


   </div>
   </div>
   </div>
  </>
  )
}

export default Login
