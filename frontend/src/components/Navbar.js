import React from "react";
import {NavLink} from 'react-router-dom'

export const Navbar = () => {

    return (
        <nav>
            <div className="nav-wrapper teal darken-2">
                <NavLink to="/" className="brand-logo brand-logo-custom">ШНУР</NavLink>
                <ul id="nav-mobile" className="right hide-on-med-and-down">
                    <li><NavLink to="/data" >Данные</NavLink></li>
                    <li><NavLink to="/questions" >Анализ</NavLink></li>
                </ul>
            </div>
        </nav>
    )
}