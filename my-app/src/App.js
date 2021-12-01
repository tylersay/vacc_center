import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from './components/Login';
import Booking from './components/Booking';



function App() {
  

  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login/>} />
        <Route path="/booking" element={<Booking />} />
      </Routes>
    </Router>
  );
}

export default App;
