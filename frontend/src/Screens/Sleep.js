import React from "react";
import CurrentTime from "../components/currentTime";
import "./screen.css";
import logo from "./logo/DC_Logo.jpg"

const Sleep = (props) => {
    return(
        <div className="sleep" id="sleep">
            <div className="logo" id="logo">
                <img src={logo} alt="logo"/>
            </div>
            <div className="time" id="time">
                <CurrentTime/>
            </div>
        </div>

    )
};

export default Sleep;