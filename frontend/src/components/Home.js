import React from "react";
import { Link, useLocation } from "react-router-dom";
import '../App.css'


const Home = () => {
    const location = useLocation()
    const path = location.pathname
    return (
        <div id="appButton"><button  component = {Link} to='/application' selected = {'/application'===path}>Click Here</button>to start your application</div>
    )

}

export default Home