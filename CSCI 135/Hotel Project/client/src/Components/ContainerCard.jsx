import { Card } from "react-bootstrap"

const ContainerCard = ( { title, body } ) => {
  return (
    <Card className="h-100 w-100" style={
        {   width: '22rem', 
            backgroundColor: "hsla(240, 10%, 18%, 0.815)"
        }
    }>
      <Card.Header className="text-center mh-100"> {title} </Card.Header>
      <Card.Body className="h-100" style={{padding: "0.5rem" }}>
        {body}
      </Card.Body>
    </Card>
  )
}

export default ContainerCard