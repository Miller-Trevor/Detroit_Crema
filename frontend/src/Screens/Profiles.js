import React from "react"
import ProfilePage from "./ProfilePage1";
import {useNavigate} from 'react-router-dom';

function Profiles(){
    const navigate = useNavigate();

    return(
        <div className="profiles" id="profiles">
            <button className="profilesButton" id="profilesButton" onClick={() => navigate("/profilepage1")}>Profile 1</button>
            <button className="profilesButton" id="profilesButton" onClick={() => navigate("/profilepage2")}>Profile 2</button>
            <button className="profilesButton" id="profilesButton" onClick={() => navigate("/profilepage3")}>Profile 3</button>
        </div>

    
    )
}

export default Profiles;