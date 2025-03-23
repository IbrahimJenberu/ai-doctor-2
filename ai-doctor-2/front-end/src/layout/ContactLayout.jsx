import React from 'react'
import Contactpage from '../pages/Contactpage'
import { Outlet } from 'react-router-dom'

const ContactLayout = () => {
  return (
    <div>
<Contactpage/>
<div>
    <Outlet/>
</div>
    </div>
  )
}

export default ContactLayout