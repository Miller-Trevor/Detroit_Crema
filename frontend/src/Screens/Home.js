import CurrentTime from "../components/currentTime"
import logo from "./logo/DC_Logo.jpg"

const Home = (props) => {

    return(
        <div className="home" id="home">
            <div className="homeLogo" id="homeLogo">
                <img src={logo} alt="logo"/>
            </div>
            <div id="timeButton" className="timeButton">
                <button className="previousBrew" id="previousBrew"> Previous Brew <br/> Preinfusion <br/> bar, time <br/> Peak Pressure <br/> peak, end </button>
                <button className="currentTime" id="currentTime"><CurrentTime/></button>
            </div>
        </div>

    )
}

export default Home;