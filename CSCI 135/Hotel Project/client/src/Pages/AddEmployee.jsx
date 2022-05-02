import { Container, Form, Button, Table, Card, Row, Col } from "react-bootstrap"
import { useState } from "react"
import axios from "axios"
import { Alert, Spinner } from "react-bootstrap"
import { useNavigate } from "react-router-dom";


const AddEmployee = () => {
    const [message, setMessage] = useState({ type: "", header: "", body: "" });
    const [showAlert, setShowAlert] = useState(false);

    const navigate = useNavigate();

    const  onFormSubmit = async e => {
        e.preventDefault()
        const formData = new FormData(e.target),
        formDataObj = Object.fromEntries(formData.entries())
        try {
            const res = await axios.post("/api/add/employee", formDataObj, {
              headers: { "Content-Type" : "application/json" },  
              })
            setShowAlert(true)
            setMessage(
              {
                type: "success",
                header: "File Uploaded Successful'y",
                body: "Your export file was uploaded to the server! Please wait for the dashboard to redirect you once parsing is complete!"
              }
            )
            setTimeout(() => {
              navigate("/employees", { replace: true });
            }, 1000)
          } 
          catch (err) {
            if (err.response.status === 500){
              setShowAlert(true)
              setMessage(
                {
                  type: "danger",
                  header: "Oh snap! There was an internal issue with the server!",
                  body: "We didn't get a response from the server! Make sure that the server is up and running before uploading your file!"
                }
              )
            } 
            if (err.response.status === 400){
              setShowAlert(true)
              setMessage(
                {
                  type: "danger",
                  header: "Oh snap! This file could not be read!",
                  body: "This file could not be parsed by the sever. Make sure that this file is an Apple Health Export zip file!"
                }
              )
            }
            else {
              setShowAlert(true)
              setMessage(
                {
                  type: "danger",
                  header: " Oh snap! Unknown Error",
                  body: (err.response.data.msg)
                }
              )
            }
          } 
    }
    return (
      <div>
        <Container>
            <Card>
                <Card.Header>
                    Add Employee Form
                </Card.Header>
                <Card.Body>
                    <Form onSubmit={onFormSubmit}>
                        <Row>
                            <Col>
                                <Form.Group className="mb-3" controlId="formFirstName">
                                    <Form.Label>First Name</Form.Label>
                                    <Form.Control name="First Name" type="text" placeholder="First name" />
                                </Form.Group>
                            </Col>
                            <Col xs={1}>
                                <Form.Group className="mb-3" controlId="formMiddleInitial">
                                    <Form.Label>M.I</Form.Label>
                                    <Form.Control name="Middle Initial" type="text" placeholder="M.I" />
                                </Form.Group>
                            </Col>
                            <Col>
                                <Form.Group className="mb-3" controlId="formLastName">
                                    <Form.Label>Last Name</Form.Label>
                                    <Form.Control name="Last Name" type="text" placeholder="Last name" />
                                </Form.Group>
                            </Col>
                        </Row>
                        <Row>
                            <Col>
                                <Form.Group className="mb-3" controlId="formPhoneNumber">
                                    <Form.Label>Phone Number</Form.Label>
                                    <Form.Control name="Phone Number" type="text" placeholder="Phone Number" />
                                </Form.Group>
                            </Col>
                            <Col>
                                <Form.Group className="mb-3" controlId="formEmail">
                                    <Form.Label>Email </Form.Label>
                                    <Form.Control name="Email" type="email" placeholder="Email" />
                                </Form.Group>
                            </Col>
                            <Col>
                                <Form.Group className="mb-3" controlId="formDateOfBirth">
                                    <Form.Label>DOB YYYY-DD-MM</Form.Label>
                                    <Form.Control name="Date of Birth" type="text" placeholder="Date of Birth" />
                                </Form.Group>
                            </Col>
                        </Row>
                        <Row>
                            <Col xs={3}>
                                <Form.Group className="mb-3" controlId="formSocialSecurityNumber">
                                    <Form.Label>SSN</Form.Label>
                                    <Form.Control name="SSN" type="password" placeholder="SSN" />
                                </Form.Group>
                            </Col>
                            <Col>
                                <Form.Group className="mb-3" controlId="formAddress">
                                    <Form.Label>Address</Form.Label>
                                    <Form.Control name="Address" type="Address" placeholder="Enter address" />
                                </Form.Group>
                            </Col>
                        </Row>
                        <Row>
                            <Col>
                                <Form.Group className="mb-3">
                                    <Form.Label>Occupation</Form.Label>
                                    <Form.Select name="Occupation">
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
                                    <Form.Select name="Occupation Steps">
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
                        <Button variant="primary" type="submit">
                            Submit
                        </Button>
                    </Form>
                </Card.Body>
            </Card>
   
        </Container>
      </div>
    )
    
  }
  
  export default AddEmployee