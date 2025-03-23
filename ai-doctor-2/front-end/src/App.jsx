
import './App.css'
import Homepage from './pages/Homepage'
import { createBrowserRouter, createRoutesFromElements, Route,RouterProvider,Routes } from 'react-router-dom'

import Aboutpage from './pages/Aboutpage'
import Contactpage from './pages/Contactpage'
import Login from './pages/Login'
import Servicespage from './pages/Servicespage'
import RootLayout from './layout/RootLayout'
import Contactinfo from './components/Contactinfo'
import Contactform from './components/Contactform'
import ContactLayout from './layout/ContactLayout'
import Notfound from './components/Notfound'
import LoginLayout from './layout/LoginLayout'


const App = () => {
const router =createBrowserRouter(createRoutesFromElements(
  // <Route path='/' element={<RootLayout/>}>
  //     <Route  index element={<Homepage/>} />
  //     <Route  path='About' element={<Aboutpage/>} />
  //     <Route  path='Services' element={<Servicespage/>} />
  //     <Route  path='Contact' element={<ContactLayout/>}>

  //          <Route  path='Info' element={<Contactinfo/>}/>
  //          <Route  path='Form' element={<Contactform/>}/>
    
  // </Route>
  // <Route  path='*' element={<Notfound/>} />
  // </Route>
  <Route>
  {/* Root layout with Navbar */}
  <Route path='/' element={<RootLayout />}>
    <Route index element={<Homepage />} />
    <Route path='About' element={<Aboutpage />} />
    <Route path='Services' element={<Servicespage />} />
    <Route path='Contact' element={<ContactLayout />}>
      <Route path='Info' element={<Contactinfo />} />
      <Route path='Form' element={<Contactform />} />
    </Route>
  </Route>

  {/* Login layout without Navbar */}
  <Route path='/login' element={<LoginLayout />}>
    <Route index element={<Login />} />
  </Route>

  {/* Not found route */}
  <Route path='*' element={<Notfound />} />
</Route>
))
  return (
   <RouterProvider router={router} />
  )
}

export default App