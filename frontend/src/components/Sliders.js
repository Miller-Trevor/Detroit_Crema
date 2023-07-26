import React from "react";
import {useState} from "react";

function Sliders() {

    const [point1, setPoint1] = useState(3);
    const [point2, setPoint2] = useState(3);
    const [point3, setPoint3] = useState(3);
    const [point4, setPoint4] = useState(3);
    const [point5, setPoint5] = useState(3);
    
    return(
        <div className="sliders">
            <div style={{paddingLeft: 55, paddingRight: 55, display: 'flex', justifyContent: 'space-between'}}>
                <text>{point1}</text>
                <text>{point2}</text>
                <text>{point3}</text>
                <text>{point4}</text>
                <text>{point5}</text>
            </div>
            <div style={{marginTop:80, display: 'flex', justifyContent: 'space-between'}}>
                <input
                    max={10}
                    type='range'
                    value={point1}
                    onChange={(e) => setPoint1(e.target.value)}
                    style={{ transform: 'rotate(270deg)' }}
                />
                <input
                    max={10}
                    type='range'
                    value={point2}
                    onChange={(e) => setPoint2(e.target.value)}
                    style={{ transform: 'rotate(270deg)' }}
                />
                <input
                    max={10}
                    type='range'
                    value={point3}
                    onChange={(e) => setPoint3(e.target.value)}
                    style={{ transform: 'rotate(270deg)' }}
                />
                <input
                    max={10}
                    type='range'
                    value={point4}
                    onChange={(e) => setPoint4(e.target.value)}
                    style={{ transform: 'rotate(270deg)' }}
                />
                <input
                    max={10}
                    type='range'
                    value={point5}
                    onChange={(e) => setPoint5(e.target.value)}
                    style={{ transform: 'rotate(270deg)' }}
                />
            </div>
        </div>
    );
};

export default Sliders;
