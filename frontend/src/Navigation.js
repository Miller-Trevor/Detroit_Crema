import React from 'react';
import {Nav, NavItem} from 'reactstrap'
import { NavLink } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faGear, faMoon, faMugHot, faHome, faUserCircle } from '@fortawesome/free-solid-svg-icons';
import './App.css';

const tabs = [{
  route: "/home",
  icon: faHome,
  label: "Home"
},{
    route: "/brew",
    icon: faMugHot,
    label: "Brew"
},{
    route: "/profiles",
    icon: faUserCircle,
    label: "Profiles"
},{
    route: "/settings", 
    icon: faGear,
    label: "Settings"
}
]

const Navigation = (props) => {
    return (
        <div>
          {/* Bottom Tab Navigator*/}
          <nav className="navbar fixed-bottom navbar-light" role="navigation">
            <Nav className="w-100">
              <div className=" d-flex flex-row justify-content-around w-100">
                {
                  tabs.map((tab, index) =>(
                    <NavItem key={`tab-${index}`}>
                      <NavLink to={tab.route} className="nav-link bottom-nav-link" activeClassName="active">
                        <div className="row d-flex flex-column justify-content-center align-items-center">
                          <FontAwesomeIcon size="lg" icon={tab.icon}/>
                          <div className="bottom-tab-label">{tab.label}</div>
                        </div>
                      </NavLink>
                    </NavItem>
                  ))
                }
              </div>
            </Nav>
          </nav>
        </div>
      )
    };

    export default Navigation;