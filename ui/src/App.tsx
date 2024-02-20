import './App.scss'
import {Route, Routes} from 'react-router-dom'
import Navbar from './components/Navbar/navbar'
import Home from './pages/Home'
import Games from './pages/Games'
import Items from './pages/Items'

export default function App() {

  return (
    <>
      <Navbar />
      <div className="container">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/games" element={<Games />} />
          <Route path="/items" element={<Items />} />
        </Routes>
      </div>
    </>
  )
}


