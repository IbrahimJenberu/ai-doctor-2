import React from 'react'
import { useNavigate } from 'react-router-dom'

const Notfound = () => {
    const navigate=useNavigate();
  return (
    <div>
   <h1  >404|page not found</h1>
   <h1  >404|page not found</h1>
   <button onClick={()=>navigate('/')}>Go to Homepage</button>
    </div>

  )
}

export default Notfound