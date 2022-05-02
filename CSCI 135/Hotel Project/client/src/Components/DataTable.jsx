import { Table } from "react-bootstrap"

const DataTable = ( {data} ) => {
  return (
    <Table bordered className="h-100 w-100 table-responsive overflow-visible">
        <tbody className="h-100 mb-3">
            {Object.keys(data).map((key) => {  
                return (
                    <tr style={{color: "white"}}>
                        <td key={key}> {key} </td>
                        <td key={key}> {data[key]} </td>
                    </tr>
                )
            })}
        </tbody>
    </Table>
  )
}

export default DataTable