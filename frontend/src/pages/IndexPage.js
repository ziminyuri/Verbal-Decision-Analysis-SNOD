import React from "react";
import {NavLink} from 'react-router-dom'
import {Navbar} from "../components/Navbar";


export const IndexPage =() => {
    return (


        <div>
            <Navbar />
            <h1>Главная страница</h1>
            <div className="row">
            <div className="col s6 m6">
                        <div className="card blue-grey darken-1">
                            <div className="card-content white-text">
                                <span className="card-title">Ввести пользовательские данные</span>
                                <p>I am a very simple card. I am good at containing small bits of information.
                                    I am convenient because I require little markup to use effectively.</p>
                            </div>
                            <div className="card-action">
                                <NavLink to="/model/create">Ввести в приложении</NavLink>
                                <a href="#">Загрузить .csv</a>
                            </div>
                        </div>
            </div>
            <div className="col s6 m6">
                        <div className="card blue-grey darken-1">
                            <div className="card-content white-text">
                                <span className="card-title">Использовать Демо данные</span>
                                <p>I am a very simple card. I am good at containing small bits of information.
                                    I am convenient because I require little markup to use effectively.</p>
                            </div>
                            <div className="card-action">
                                <NavLink to="/data" >Использовать</NavLink>
                            </div>
                        </div>
            </div>
            </div>
        </div>
    )
}