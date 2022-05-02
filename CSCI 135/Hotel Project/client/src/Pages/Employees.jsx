import { Container, Table, Card, Row, Col } from "react-bootstrap"
import { Link } from "react-router-dom"
import axios from "axios"
import { useState, useEffect } from "react"

const Employees = () => {
    const [employeeTable, setEmployeeTable] = useState({})


    useEffect(() => {
        const getAllEmployees = async () => {
          const allEmployees = await axios("/api/get/employees")
          setEmployeeTable(allEmployees.data)   
          }
          getAllEmployees()
      }, [])
    
    return (
      <>
        <Container fluid>
            <Card>
                <Card.Header>
                    Manage Employees
                </Card.Header>
                <Card.Body>
                    <>
                        <div className="mb-2 d-flex justify-content-end"> 
                            <Link to="/add-employee">
                                <button 
                                    type="button" 
                                    className="btn btn-success"> 
                                    Add Employee
                                </button> 
                            </Link>
                            <Link to="/modify-employee">
                                <button 
                                    type="button" 
                                    className="btn btn-danger ml-2"> 
                                    Modify Employee
                                </button>
                            </Link>
                        </div>
                        <div>
                            <Table striped bordered hover>
                                <thead>
                                    <tr>
                                        <th colSpan={1}> ID </th>
                                        <th> Name </th>
                                        <th> Job </th>
                                        <th> Age </th>
                                        <th> Phone </th>
                                        <th> Email </th>
                                        <th> Salary </th>
                                        <th> SSN </th>
                                    </tr>
                                </thead>
                                <tbody>
                                {Object.keys(employeeTable).map((key) => {  
                                    console.log(key)
                                    return (
                                        <tr>
                                            <td key={key} colSpan={1}> {employeeTable[key]["id"]} </td>
                                            <td key={key}> {employeeTable[key]["name"]} </td>
                                            <td key={key}> {employeeTable[key]["job"]} </td>
                                            <td key={key}> {employeeTable[key]["age"]} </td>
                                            <td key={key}> {employeeTable[key]["phone"]} </td>
                                            <td key={key}> {employeeTable[key]["email"]} </td>
                                            <td key={key}> {employeeTable[key]["salary"]} </td>
                                            <td key={key}> {employeeTable[key]["ssn"]} </td>
                                        </tr>
                                    )
                                })}
                                </tbody>
                            </Table>
                        </div>
                    </>
                </Card.Body>
            </Card>
        </Container>
      </>
    )
    
  }
  
  export default Employees