import LineChart from '../components/LineChart';
import {useState} from 'react'
import React from 'react';
import Sliders from '../components/Sliders';
import Axios from 'axios';

const Brew = (props) => {

const [temperature, setTemperature] = useState(70);
const [volume, setVolume] = useState(20);
const [time1, setTime1] = useState(15);
const [time2, setTime2] = useState(25);
const [time3, setTime3] = useState(30);
const [time4, setTime4] = useState(40);
const [time5, setTime5] = useState(60);
const [wakeUp, setWakeUp] = useState("");
const [sleep, setSleep] = useState("");
const [preinfusePressure, setPreinfusePressure] = useState(0);
const [preinfuseTime, setPreinfuseTime] = useState(0);
const [point1, setPoint1] = useState(3);
const [point2, setPoint2] = useState(3);
const [point3, setPoint3] = useState(3);
const [point4, setPoint4] = useState(3);
const [point5, setPoint5] = useState(3);

const handleTemperature = (event) => {
  setTemperature(event.target.value);
};

const handleVolume = (event) => {
  setVolume(event.target.value);
};

const handleWakeUp = (event) => {
  setWakeUp(event.target.value);
};

const handleSleep = (event) => {
  setSleep(event.target.value);
};

const handlePreinfusePressure = (event) => {
  setPreinfusePressure(event.target.value);
};

const handleTime1 = (event) => {
  setTime1(event.target.value);
};

const handleTime2 = (event) => {
  setTime2(event.target.value);
};

const handleTime3 = (event) => {
  setTime3(event.target.value);
};

const handleTime4 = (event) => {
  setTime4(event.target.value);
};

const handleTime5 = (event) => {
  setTime5(event.target.value);
};

const addProfile = () => {
  Axios.post("http://localhost:3001/create", {
  point1: point1,
  point2: point2, 
  point3: point3,
  point4: point4,
  point5: point5,
  time1: time1,
  time2: time2,
  time3: time3,
  time4: time4,
  time5: time5,
  }).then(() => {
    console.log("Logged");
  });
};

  return (
    <div className="brew">
      <div className="sliders">
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
      <div style={{paddingLeft: 55, paddingRight: 55, marginTop: 60, display: 'flex', justifyContent: 'space-between'}}>
        {/* <text>{preinfuseTime}</text>
        <text>{time2}</text>
        <text>{time3}</text>
        <text>{time4}</text>
        <text>{maxTime}</text> */}
        <input className='graphTime' id='graphTime' type='number' placeholder='15' onChange={handleTime1}></input>
        <input className='graphTime' id='graphTime' type='number' placeholder='15' onChange={handleTime2}></input>
        <input className='graphTime' id='graphTime' type='number' placeholder='15' onChange={handleTime3}></input>
        <input className='graphTime' id='graphTime' type='number' placeholder='15' onChange={handleTime4}></input>
        <input className='graphTime' id='graphTime' type='number' placeholder='15' onChange={handleTime5}></input>
      </div>
      <div style={{height: 200, width: 700, marginLeft: 250}}>
        <LineChart p1={point1} p2={point2} p3={point3} p4={point4} p5={point5} t1={time1} t2={time2} t3={time3} t4={time4} t5={time5}/>
      </div>
      <div>
        <button className='button' id='button'type="button" onClick={addProfile}>Brew</button>
      </div>
      {/* <div className='input' id='input'>
        <input className='boxes' id='boxes' type='number' placeholder='Preinfusion Pressure' onChange={handlePreinfusePressure}></input>
        <input className='boxes' id='boxes' type='number' placeholder='Preinfusion Time'></input>
      </div>
      <div className='input' id='input'>
        <input className='boxes' id='boxes' type='number' placeholder='Max Time'></input>
      </div>
      <div className='input' id='input'>
        <button className='button' id='button'type="button">Steam</button>
        <input className='boxes' id='boxes' type='number' placeholder='Temperature' onChange={handleTemperature}></input>
        <input className='boxes' id='boxes' type='number' placeholder='Volume' onChange={handleVolume}></input>
        <button className='button' id='button'type="button">Brew</button>
      </div>
      <div className='input' id='input'>
        <input className='boxes' id='boxes' type='time' placeholder='Wake-Up' onChange={handleWakeUp}></input>
        <input className='boxes' id='boxes' type='time' placeholder='Sleep' onChange={handleSleep}></input>
      </div>*/}
    </div> 
  )
}

export default Brew;