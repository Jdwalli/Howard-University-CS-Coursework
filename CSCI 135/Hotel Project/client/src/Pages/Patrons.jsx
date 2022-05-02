import { Container, Button, Card, Form, Row, Col } from "react-bootstrap"


const Patrons = () => {
    return (
      <>
        <Container fluid>
          <Row className="mb-3" style={{height: "450px"}}> 
            <Card> 
              <Card.Header> Hotel Room Breakdown </Card.Header>
              <Card.Body>

              </Card.Body>
            </Card>
          </Row>
          <Row style={{height: "550px"}}>
            <Col>
              <Card>
                <Card.Header> Book Patron Today</Card.Header>
                <Card.Body> 
                  <Row>
                    <Form.Group className="mb-2" controlId="formTodayBookRoomNumber">
                      <Form.Label>Room Number</Form.Label>
                      <Form.Control type="text" placeholder="Room Number" />
                    </Form.Group>
                  </Row>
                  <Row>
                    <Form.Group className="mb-2" controlId="formTodayBookRoomName">
                      <Form.Label>Room Name</Form.Label>
                      <Form.Control type="text" placeholder="Room Name" />
                    </Form.Group>
                  </Row>
                  <Row>
                    <Form.Group className="mb-2" controlId="formTodayBookNumberOfAdults">
                      <Form.Label>Number of Adults</Form.Label>
                      <Form.Control type="text" placeholder="Number of Adults" />
                    </Form.Group>
                  </Row>
                  <Row>
                    <Form.Group className="mb-2" controlId="formTodayBookNumberOfChildren">
                      <Form.Label>Number of Children</Form.Label>
                      <Form.Control type="text" placeholder="Number of Children" />
                    </Form.Group>
                  </Row>
                  <Row>
                    <Form.Group className="mb-3" controlId="formTodayBookEndDate">
                      <Form.Label> Check out Date </Form.Label>
                      <Form.Control type="text" placeholder="Check out date" />
                    </Form.Group>
                  </Row>
                  <Row>
                      <Button variant="primary" type="submit">
                        Submit Bookings
                      </Button>
                  </Row>
                </Card.Body>
              </Card>
            </Col>
            <Col>
              <Card>
                <Card.Header> Book Future Reservation </Card.Header>
                <Card.Body> 
                  <Row>
                    <Form.Group className="mb-2" controlId="formFutureBookRoomNumber">
                      <Form.Label>Room Number</Form.Label>
                      <Form.Control type="text" placeholder="Room Number" />
                    </Form.Group>
                  </Row>
                  <Row>
                    <Form.Group className="mb-2" controlId="formFutureBookRoomName">
                      <Form.Label>Room Name</Form.Label>
                      <Form.Control type="text" placeholder="Room Name" />
                    </Form.Group>
                  </Row>
                  <Row>
                    <Form.Group className="mb-2" controlId="formFutureBookNumberOfAdults">
                      <Form.Label>Number of Adults</Form.Label>
                      <Form.Control type="text" placeholder="Number of Adults" />
                    </Form.Group>
                  </Row>
                  <Row>
                    <Form.Group className="mb-2" controlId="formFutureBookNumberOfChildren">
                      <Form.Label>Number of Children</Form.Label>
                      <Form.Control type="text" placeholder="Number of Children" />
                    </Form.Group>
                  </Row>
                  <Row>
                    <Col>
                      <Form.Group className="mb-2" controlId="formFutureBookStartDate">
                        <Form.Label> Check in Date </Form.Label>
                        <Form.Control type="text" placeholder="Check in date" />
                      </Form.Group>
                    </Col>
                    <Col>
                      <Form.Group className="mb-3" controlId="formFutureBookEndDate">
                        <Form.Label> Check out Date </Form.Label>
                        <Form.Control type="text" placeholder="Check out date" />
                      </Form.Group>
                    </Col>
                  </Row>
                  <Row>
                      <Button variant="primary" type="submit">
                        Submit Bookings
                      </Button>
                  </Row>
                </Card.Body>
              </Card>
            </Col>
            <Col>
              <Card>
                <Card.Header> Room Statistics</Card.Header>
                <Card.Body> 
                  <Row>
                    <Form.Group className="mb-2" controlId="formStatsRoomNumber">
                      <Form.Label>Room Number</Form.Label>
                      <Form.Control type="text" placeholder="Room Number" />
                    </Form.Group>
                  </Row>
                  <Row>
                    <Form.Group className="mb-2" controlId="formStatsRoomType">
                      <Form.Label>Room Type</Form.Label>
                      <Form.Control type="text" placeholder="Room Type" />
                    </Form.Group>
                  </Row>
                  <Row>
                    <Form.Group className="mb-2" controlId="formStatsFloorNumber">
                      <Form.Label>Floor Number</Form.Label>
                      <Form.Control type="text" placeholder="Floor Number" />
                    </Form.Group>
                  </Row>
                  <Row>
                    <Form.Group className="mb-2" controlId="formStatsWifiIncluded">
                      <Form.Label>Wifi Included?</Form.Label>
                      <Form.Control type="text" placeholder="Is Wifi Included?" />
                    </Form.Group>
                  </Row>
                  <Row>
                    <Col>
                      <Form.Group className="mb-2" controlId="formStatsRoomStatus">
                        <Form.Label> Room Status </Form.Label>
                        <Form.Control type="text" placeholder="Room Status" /> 
                      </Form.Group>
                    </Col>
                  </Row>
                  <Row>
                      <Button variant="primary" type="submit">
                        Search Room
                      </Button>
                  </Row>
                </Card.Body>
              </Card>
            </Col>
          </Row>
        </Container>
      </>
    )
    
  }
  
  export default Patrons