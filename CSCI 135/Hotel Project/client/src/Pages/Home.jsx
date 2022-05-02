import { Container, Table, Card, Row, Col } from "react-bootstrap"
import Donut from "../Components/Charts/Donut"

const Home = () => {
    return (
      <div>
        <Container fluid>
            <Row className="mb-2 d-flex">
                <Col xs={5}> 
                    <Card>
                        <Card.Header> Reservations </Card.Header>
                        <Card.Body> 
                            <Row>
                                <Col> 
                                    <Donut />
                                </Col>
                                <Col>
                                    Stats
                                </Col>
                            </Row>
                        </Card.Body>
                    </Card>
                </Col>
                <Col>
                    <Card>
                        <Card.Header> Rooms </Card.Header>
                        <Card.Body>
                            <Table striped bordered hover>
                                <thead>
                                    <tr>
                                        <th>Type</th>
                                        <th> Available </th>
                                        <th> Sold </th>
                                        <th> Maintenance </th>
                                        <th> Total </th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {/* <tr>
                                        <td></td>
                                    </tr> */}
                                </tbody>
                            </Table>
                        </Card.Body>
                    </Card>
                </Col>
            </Row>
            <Row className="mb-2 d-flex">
                <Col>
                    <Card>
                        <Card.Header> Reservation Types </Card.Header>
                        <Card.Body>
                            <Donut />
                            <section className="d-flex mb-0">
                                <p className="mb-0"> Guests </p>
                                <p className="mb-0" style={{marginLeft: "auto"}}> 0 </p>
                            </section>
                            <hr style={{margin: 0}}/>
                            <section className="d-flex mb-0 mt-2">
                                <p className="mb-0"> Adults </p>
                                <p className="mb-0" style={{marginLeft: "auto"}}> 0 </p>
                            </section>
                            <hr style={{margin: 0}}/>
                            <section className="d-flex mb-0 mt-2">
                                <p className="mb-0"> Children </p>
                                <p className="mb-0" style={{marginLeft: "auto"}}> 0 </p>
                            </section>
                            <hr style={{margin: 0}}/>
                        </Card.Body>
                    </Card>
                </Col>
                <Col>
                    <Card>
                        <Card.Header> House Keeping </Card.Header>
                        <Card.Body>
                            <Donut />
                            <section className="d-flex mb-0">
                                <p className="mb-0"> Clean </p>
                                <p className="mb-0" style={{marginLeft: "auto"}}> 0 </p>
                            </section>
                            <hr style={{margin: 0}}/>
                            <section className="d-flex mb-0 mt-2">
                                <p className="mb-0"> Cleaning </p>
                                <p className="mb-0" style={{marginLeft: "auto"}}> 0 </p>
                            </section>
                            <hr style={{margin: 0}}/>
                            <section className="d-flex mb-0 mt-2">
                                <p className="mb-0"> Dirty </p>
                                <p className="mb-0" style={{marginLeft: "auto"}}> 0 </p>
                            </section>
                            <hr style={{margin: 0}}/>
                        </Card.Body>
                    </Card>
                </Col>
                <Col>
                    <Card>
                        <Card.Header> Services </Card.Header>
                        <Card.Body>
                        </Card.Body>
                    </Card>
                </Col>
            </Row>
            <Row>
                <Col>
                    <Card>
                        <Card.Header> Total Earnings </Card.Header>
                    </Card>
                </Col>
                <Col>
                    <Card>
                        <Card.Header> Monthly Earnings </Card.Header>
                    </Card>
                </Col>
                <Col>
                    <Card>
                        <Card.Header> Guests Per Day </Card.Header>
                    </Card>
                </Col>
            </Row>

        </Container>
      </div>
    )
    
  }
  
  export default Home