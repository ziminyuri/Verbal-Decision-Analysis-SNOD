import React, {useContext} from "react";
import {NavLink, useHistory} from 'react-router-dom'
import {AuthContext} from "../context/AuthContext";

export const Navbar = () => {
    const history = useHistory()
    const auth = useContext(AuthContext)

    const logoutHandler = event => {
        event.preventDefault()
        auth.logout()
        history.push('/')
    }

    return (
        <nav>
            <div className="nav-wrapper teal darken-2">
                <NavLink to="/" className="brand-logo brand-logo-custom">ШНУР</NavLink>
                <ul id="nav-mobile" className="right hide-on-med-and-down">
                    <li><NavLink to="/" >Главная</NavLink></li>
                    <li><NavLink to="/models" >Модели</NavLink></li>
                    <li><a href='/' onClick={logoutHandler} >Выйти</a></li>
                </ul>
            </div>
        </nav>
    )
}