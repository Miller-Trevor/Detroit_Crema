import './App.css';
import {BrowserRouter as Router, Routes, Route} from "react-router-dom"
import React from "react";
import Home from './Screens/Home';
import Sleep from './Screens/Sleep';
import Brew from './Screens/Brew';
import Navigation from './Navigation';
import Profiles from './Screens/Profiles';
import Settings from './Screens/Settings';
import ProfilePage1 from './Screens/ProfilePage1';
import ProfilePage2 from './Screens/ProfilePage2';
import ProfilePage3 from './Screens/ProfilePage3';

function App() {
 return(
  <div className="App">
    <Router>
  <Navigation />
  <Routes>
    <Route path="/home" element={<Home />}/>
    <Route path="/settings" element={<Settings />} />
    <Route path="/brew" element={<Brew />} />
    <Route path="/profiles" element={<Profiles />}/>
    <Route path="/profilepage1" element={<ProfilePage1/>}/>
    <Route path="/profilepage2" element={<ProfilePage2/>}/>
    <Route path="/profilepage3" element={<ProfilePage3/>}/>
  </Routes>
</Router>
  </div>
  )
}

export default App;
