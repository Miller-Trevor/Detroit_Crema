import React from "react"
import CurrentTime from "../components/currentTime";


const Settings = () => {
    return (
        <div className="settings" id="settings">
            <h2 className="settingsTime" id="settingsTime"><CurrentTime/></h2>
            <div>
                <button className="settingsButton" id="settingsButton">Auto On/Off</button>
            </div>
            <div>
                <button className="settingsButton" id="settingsButton">Display Settings</button>
            </div>
        </div>
    )
}

export default Settings;