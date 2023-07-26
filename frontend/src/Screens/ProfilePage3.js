import React, {useState, useEffect} from "react";
import LineChart from "../components/LineChart";

import axios from 'axios';

const ProfilePage3 = (props) => {
    const [rowData, setRowData] = useState({});
    const rowId = 3;
    useEffect(() => {
        axios.get('http://localhost:3001/api/data/${rowId}')
            .then(response => setRowData(response.data))
            .catch(error => console.error('Error fetching data: ', error));
    }, [rowId]);
    
    return(
        <div className="profilepage" id="profilepage">
            <label>{rowData.id}</label>
            <LineChart p1={rowData.point1} p2={rowData.point2} p3={rowData.point3} p4={rowData.point4} p5={rowData.point5} t1={rowData.time1} t2={rowData.time2} t3={rowData.time3} t4={rowData.time4} t5={rowData.time5}/>
        </div>

)}

export default ProfilePage3;