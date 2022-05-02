// Package Imports
import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import { Container, Navbar, Nav } from "react-bootstrap"

// Style imports
import './Styles/App.css';

// Routes
import Home from "./Pages/Home"
import Patrons from "./Pages/Patrons"
import Employees from "./Pages/Employees";
import Services from "./Pages/Services";
import AddEmployee from "./Pages/AddEmployee";
import ModifyEmployee from "./Pages/ModifyEmployee";


function App() {
  return (
    <Router>
      <div className="App">
        <Navbar bg="dark" variant="dark">
          <Container>
            <Navbar.Brand href="/"> [APP NAME HERE] - HOTEL MANAGEMENT SYSTEM </Navbar.Brand>
            <Nav className="justify-content-start m">
              <Nav.Link href="/"> Home </Nav.Link>
              <Nav.Link href="/patrons">Patrons</Nav.Link>
              <Nav.Link href="/employees">Employees</Nav.Link>
              <Nav.Link href="/services">Services</Nav.Link>
            </Nav>
          </Container>
        </Navbar>
      </div>
      <div className="content">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/patrons" element={<Patrons />} />
          <Route path="employees" element={<Employees />} />
          <Route path="/services" element={<Services />} />
          <Route path="/add-employee" element={<AddEmployee />} />
          <Route path="/modify-employee" element={<ModifyEmployee />} />
          
          
        </Routes>
      </div>
    </Router>
  );
}

export default App;



