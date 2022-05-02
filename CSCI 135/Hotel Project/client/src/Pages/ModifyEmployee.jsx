import { Container, Form, Button, Table, Card, Row, Col } from "react-bootstrap"

const ModifyEmployee = () => {
    return (
      <div>
        <Container>
            <Card>
                <Card.Header>
                  Modify Employee Form
                </Card.Header>
                <Card.Body>
                  <div className="mb-3">
                    <Form>
                      <Form.Group className="mb-3" controlId="formEmployeeID">
                        <Form.Label>Enter employee ID</Form.Label>
                        <Form.Control type="text" placeholder="Enter employee ID to search" />
                    </Form.Group>
                    </Form>

                  </div>
                    <Form>
                        <Row>
                            <Col>
                                <Form.Group className="mb-3" controlId="formFirstName">
                                    <Form.Label>First Name</Form.Label>
                                    <Form.Control type="text" placeholder="First name" />
                                </Form.Group>
                            </Col>
                            <Col xs={1}>
                                <Form.Group className="mb-3" controlId="formMiddleInitial">
                                    <Form.Label>M.I</Form.Label>
                                    <Form.Control type="text" placeholder="M.I" />
                                </Form.Group>
                            </Col>
                            <Col>
                                <Form.Group className="mb-3" controlId="formLastName">
                                    <Form.Label>Last Name</Form.Label>
                                    <Form.Control type="text" placeholder="Last name" />
                                </Form.Group>
                            </Col>
                        </Row>
                        <Row>
                            <Col>
                                <Form.Group className="mb-3" controlId="formPhoneNumber">
                                    <Form.Label>Phone Number</Form.Label>
                                    <Form.Control type="text" placeholder="Phone Number" />
                                </Form.Group>
                            </Col>
                            <Col>
                                <Form.Group className="mb-3" controlId="formEmail">
                                    <Form.Label>Email </Form.Label>
                                    <Form.Control type="email" placeholder="Email" />
                                </Form.Group>
                            </Col>
                            <Col>
                                <Form.Group className="mb-3" controlId="formDateOfBirth">
                                    <Form.Label>DOB YYYY-DD-MM</Form.Label>
                                    <Form.Control type="text" placeholder="Date of Birth" />
                                </Form.Group>
                            </Col>
                        </Row>
                        <Row>
                            <Col xs={3}>
                                <Form.Group className="mb-3" controlId="formSocialSecurityNumber">
                                    <Form.Label>SSN</Form.Label>
                                    <Form.Control type="password" placeholder="SSN " />
                                </Form.Group>
                            </Col>
                            <Col>
                                <Form.Group className="mb-3" controlId="formEmail">
                                    <Form.Label>Email address</Form.Label>
                                    <Form.Control type="email" placeholder="Enter email" />
                                </Form.Group>
                            </Col>
                        </Row>
                        <Row>
                            <Col>
                                <Form.Group className="mb-3">
                                    <Form.Label>Occupation</Form.Label>
                                    <Form.Select>
                                        <option>Job 1</option>
                                        <option>Job 2</option>
                                        <option>Job 3</option>
                                        <option>Job 4</option>
                                    </Form.Select>
                                </Form.Group>
                            </Col>
                            <Col>
                                <Form.Group className="mb-3">
                                    <Form.Label>Occupation salary steps</Form.Label>
                                    <Form.Select>
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
                            <Button variant="primary" type="submit">
                              Submit Modifications
                            </Button>
                          </Col>
                          <Col>
                            <Button variant="danger" type="submit">
                              Remove Employee
                            </Button>
                          </Col>
                        </Row>
                    </Form>
                </Card.Body>
            </Card>
        </Container>
      </div>
    )
    
  }
  
  export default ModifyEmployee