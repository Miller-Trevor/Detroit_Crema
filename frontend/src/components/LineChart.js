import React, { useContext } from 'react'
import {Line} from 'react-chartjs-2'
import Sliders from './Sliders';
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement } from 'chart.js';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement
);

const LineChart = (props) => {

  return(
    <div className="chart-container">
      <Line
        data={{
          labels: [props.t1, props.t2, props.t3, props.t4, props.t5],
          datasets: [
            {
              id: 1,
              label: "Pressure",
              data: [props.p1, props.p2, props.p3, props.p4, props.p5]
            }
          ] 
        }
        }
        options={{
        
            xaxis:{
                title: {
                    text: 'Time (sec)'
                }
            },

            yaxis:{
                title: {
                    text: 'Pressure (Bar)'
                }
            }, 
          plugins: {
            title: {
              display: true,
              text: "Pressure over Time"
            },
            legend: {
              display: true
            },
          }
        }}
      />
    </div>

  );
}

export default LineChart