import { Container, Button, Card, Form, Row, Col } from "react-bootstrap"


const Services = () => {
    return (
      <>
        <Container fluid>
          <Row className="mb-3">
            <Col>
              <Card style={{height: "250px"}}>
                <Card.Header> Pool </Card.Header>
                <Card.Body></Card.Body>
              </Card>
            </Col>
            <Col>
              <Card style={{height: "250px"}}>
                <Card.Header> Room Service </Card.Header>
                <Card.Body></Card.Body>
              </Card>
            </Col>
            <Col>
              <Card style={{height: "250px"}}>
                <Card.Header> Weight Room </Card.Header>
                <Card.Body></Card.Body>
              </Card>
            </Col>
            <Col>
              <Card style={{height: "250px"}}>
                <Card.Header> Day Care </Card.Header>
                <Card.Body></Card.Body>
              </Card>
            </Col>
          </Row>
          <Row className="mb-3">
            <Col>
              <Card style={{height: "250px"}}>
                <Card.Header> Conference </Card.Header>
                <Card.Body></Card.Body>
              </Card>
            </Col>
            <Col>
              <Card style={{height: "250px"}}>
                <Card.Header> WiFi </Card.Header>
                <Card.Body></Card.Body>
              </Card>
            </Col>
            <Col>
              <Card style={{height: "250px"}}>
                <Card.Header> Spa </Card.Header>
                <Card.Body></Card.Body>
              </Card>
            </Col>
            <Col>
              <Card style={{height: "250px"}}>
                <Card.Header> Tennis Courts </Card.Header>
                <Card.Body></Card.Body>
              </Card>
            </Col>
          </Row>
          <Row>
            <Col>
              <Card style={{height: "260px"}}>
                <Card.Header> Pet Daycare </Card.Header>
                <Card.Body></Card.Body>
              </Card>
            </Col>
            <Col>
              <Card style={{height: "260px"}}>
                <Card.Header> ATV Tours </Card.Header>
                <Card.Body></Card.Body>
              </Card>
            </Col>
            <Col>
              <Card style={{height: "260px"}}>
                <Card.Header> Dry Cleaning </Card.Header>
                <Card.Body></Card.Body>
              </Card>
            </Col>
            <Col>
              <Card style={{height: "260px"}}>
                <Card.Header> Valet </Card.Header>
                <Card.Body></Card.Body>
              </Card>
            </Col>
          </Row>
        </Container>
      </>
    )
    
  }
  
  export default Services