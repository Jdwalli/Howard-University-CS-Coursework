import ReactApexChart from "react-apexcharts"

function Donut(props) {
    const series =  [10, 20, 30]
    const options = {
        chart: { type: 'donut' },
        responsive: [
            {
                breakpoint: 480,
                options: {
                    chart: { width: 200 },
                legend: {
                position: 'bottom',
                locals: "bottom-right-left-top"
              }
            }
          }]
        }
    
  return ( 
        <ReactApexChart 
            type="donut" 
            options={options} 
            series={series} 
            height={'100%'} 
        />
    )
}



export default Donut