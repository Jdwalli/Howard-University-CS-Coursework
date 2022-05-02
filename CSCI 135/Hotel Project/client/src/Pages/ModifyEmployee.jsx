import { Container, Form, Button, Table, Card, Row, Col } from "react-bootstrap"
import { useState } from "react"
import axios from "axios"
import { Alert, Spinner } from "react-bootstrap"
import { useNavigate } from "react-router-dom";


const AddEmployee = () => {
    const [message, setMessage] = useState({ type: "", header: "", body: "" });
    const [showAlert, setShowAlert] = useState(false);
    const [employeeFound, setEmployeeFound] = useState(false)
    const [foundEmployeedata, setFoundEmployeeData] = useState(false)
    const [modificationValue, setModificationValue] = useState("Modify")

    const navigate = useNavigate();
    const onFormSubmitEmployeeChange = async e => {
        console.log(foundEmployeedata)
        e.preventDefault()
        const formData = new FormData(e.target),
        formDataObj = Object.fromEntries(formData.entries())
        formDataObj['Modification'] = modificationValue
        formDataObj["Index"] = foundEmployeedata.index
        formDataObj["Age"] = foundEmployeedata.Age
        formDataObj["Date of Birth"] = foundEmployeedata['Date of Birth']
        
        try {
            const res = await axios.post("/api/employee/modify", formDataObj, {
              headers: { "Content-Type" : "application/json" },  
              })
            setShowAlert(true)
            setFoundEmployeeData(res.data)
            setMessage(
              {
                type: "success",
                header: "Employee found!",
                body: "This SSN can be matched to an employee!"
              }
            )
            setEmployeeFound(true)
            setTimeout(() => {
                navigate("/employees", { replace: true });
              }, 2000)
          } 
          catch (err) {
            if (err.response.status === 400){
            setEmployeeFound(false)
              setShowAlert(true)
              setMessage(
                {
                  type: "danger",
                  header: "This employee does not exist",
                  body: "The SSN is not associated with any employee! Please look at the valid employees and enter a SSN"
                }
              )
              setTimeout(() => {
                navigate("/employees", { replace: true });
              }, 2000)
            } 
        }   
    }

    const  onFormSubmit = async e => {
        e.preventDefault()
        const formData = new FormData(e.target),
        formDataObj = Object.fromEntries(formData.entries())
        try {
            const res = await axios.post("/api/get/employee", formDataObj, {
              headers: { "Content-Type" : "application/json" },  
              })
            setShowAlert(true)
            setFoundEmployeeData(res.data)
            setMessage(
              {
                type: "success",
                header: "Employee found!",
                body: "This SSN can be matched to an employee!"
              }
            )
            setEmployeeFound(true)
          } 
          catch (err) {
            if (err.response.status === 400){
            setEmployeeFound(false)
              setShowAlert(true)
              setMessage(
                {
                  type: "danger",
                  header: "This employee does not exist",
                  body: "The SSN is not associated with any employee! Please look at the valid employees and enter a SSN"
                }
              )
              setTimeout(() => {
                navigate("/employees", { replace: true });
              }, 2000)
            } 
        } 
    }
    return (
        <>
      <div>
        <Container className="mb-3">
            <Card>
                <Card.Header>
                    Employee Lookup
                </Card.Header>
                <Card.Body>
                    <Form onSubmit={onFormSubmit}>
                        <Row>
                            <Col xs={3}>
                                <Form.Group className="mb-3" controlId="formSocialSecurityNumber">
                                    <Form.Label>SSN</Form.Label>
                                    <Form.Control name="SSN" type="password" placeholder="SSN" />
                                </Form.Group>
                            </Col>
                        </Row>
                        <Button variant="danger" type="submit">
                            Employee Lookup
                        </Button>
                    </Form>
                </Card.Body>
            </Card>
        </Container>
        </div>
        <div>
            { employeeFound === true ? (
                <Container>
                    <Card>
                        <Card.Header>
                            Modify Or Delete Employee
                    </Card.Header>
                            <Card.Body>
                                <Form onSubmit={onFormSubmitEmployeeChange}>
                                    <Row>
                                        <Form.Group className="mb-3" controlId="formFirstName">
                                            <Form.Label>First Name</Form.Label>
                                            <Form.Control name="Name" type="text" defaultValue={foundEmployeedata.Name}/>
                                        </Form.Group>
                                    </Row>
                                    <Row>
                                        <Col>
                                            <Form.Group className="mb-3" controlId="formPhoneNumber">
                                                <Form.Label>Phone Number</Form.Label>
                                                <Form.Control name="Phone Number" type="text"defaultValue={foundEmployeedata.Phone} />
                                            </Form.Group>
                                        </Col>
                                        <Col>
                                            <Form.Group className="mb-3" controlId="formEmail">
                                                <Form.Label>Email </Form.Label>
                                                <Form.Control name="Email" type="email" defaultValue={foundEmployeedata.Email} />
                                            </Form.Group>
                                        </Col>
                                        <Col>
                                            <Form.Group className="mb-3" controlId="formDateOfBirth">
                                                <Form.Label>DOB YYYY-DD-MM</Form.Label>
                                                <Form.Control name="Date of Birth" type="text" defaultValue={foundEmployeedata['Date of Birth']} />
                                            </Form.Group>
                                        </Col>
                                    </Row>
                                    <Row>
                                        <Col xs={3}>
                                            <Form.Group className="mb-3" controlId="formSocialSecurityNumber">
                                                <Form.Label>SSN</Form.Label>
                                                <Form.Control name="SSN" type="password" defaultValue={foundEmployeedata.SSN} />
                                            </Form.Group>
                                        </Col>
                                        <Col>
                                            <Form.Group className="mb-3">
                                                <Form.Label>Occupation</Form.Label>
                                                <Form.Select name="Occupation" defaultValue={foundEmployeedata['Job Title']}>
                                                    <option> Manager </option>
                                                    <option> Housekeeper </option>
                                                    <option> Cook </option>
                                                    <option> Janitor </option>
                                                    <option> Bellhop </option>
                                                    <option> Valet </option>
                                                    <option> Server </option>
                                                    <option> Security </option>
                                                    <option> Director of Services </option>
                                                </Form.Select>
                                            </Form.Group>
                                        </Col>
                                        <Col>
                                            <Form.Group className="mb-3">
                                                <Form.Label>Occupation salary steps</Form.Label>
                                                <Form.Select name="Occupation Steps" defaultValue={foundEmployeedata.SalStep}>
                                                    <option>Step 1</option>
                                                    <option>Step 2</option>
                                                    <option>Step 3</option>
                                                    <option>Step 4</option>
                                                    <option>Step 5</option>
                                                    <option>Step 6</option>
                                                    <option>Step 7</option>
                                                    <option>Step 8</option>
                                                    <option>Step 9</option>
                                                    <option>Step 10</option>
                                                </Form.Select>
                                            </Form.Group>
                                        </Col>
                                    </Row>
                                    <Row>
                                        <Col>
                                            <Form.Group className="mb-3" controlId="formEmployeeID">
                                                <Form.Label>Index</Form.Label>
                                                <Form.Control name="index" type="text" defaultValue={foundEmployeedata.index} disabled/>
                                            </Form.Group>
                                        </Col>
                                        <Col>
                                            <Form.Group className="mb-3" controlId="formSalaryInfo">
                                                <Form.Label>Salary</Form.Label>
                                                <Form.Control name="" type="text"  defaultValue={foundEmployeedata.Salary} disabled/>
                                            </Form.Group>
                                        </Col>
                                        <Col>
                                            <Form.Group className="mb-3" controlId="formEmployeeAge">
                                                <Form.Label>Age</Form.Label>
                                                <Form.Control name="age" type="text" defaultValue={foundEmployeedata.Age} disabled/>
                                            </Form.Group>
                                        </Col>
                                    </Row>
                                    <Row>
                                        <Col>
                                            <Button variant="primary" type="submit" onClick={() => {
                                                setModificationValue("Modify")
                                            }}>
                                                Submit Modifications 
                                            </Button>
                                        </Col>
                                        <Col>
                                            <Button variant="danger" type="submit" onClick={() => {
                                                setModificationValue("Fire")
                                            }}>
                                                Fire
                                            </Button>
                                        </Col>
                                    </Row>
                                </Form>
                            </Card.Body>
                        </Card>
                </Container>
            ) : (<div> </div>)
            
        
            }



        </div>

    </>     
    )
    
  }
  
  export default AddEmployee