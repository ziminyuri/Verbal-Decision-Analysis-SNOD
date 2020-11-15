import React from "react";
import {NavLink, useHistory} from 'react-router-dom'
import {useHttp} from "../hooks/http.hook";



export const IndexPage =() => {
    const {loading, request, error, clearError} = useHttp()
    const history = useHistory()

    const useDemoModelHandler = async () => {
        try {
            await request('http://127.0.0.1:8000/api/v1/model/demo/create', 'GET', )
            history.push('/model/demo')
        } catch (e) {}
    }

    return (


        <div>
            <h1>Главная страница</h1>
            <div className="row">
            <div className="col s6 m6">
                        <div className="card blue-grey darken-1">
                            <div className="card-content white-text">
                                <span className="card-title">Ввести пользовательские данные</span>
                                <p>Вы можете ввести свои данные через форму или загрузить данные с помощью .csv файла.</p>
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
                                <span className="card-title">Использовать демо данные</span>
                                <p>В демо версии предлагается 7 криетриев и 4 альтернативы</p>
                            </div>
                            <div className="card-action">
                                <button
                                onClick={useDemoModelHandler}>Использовать</button>
                            </div>
                        </div>
            </div>
            </div>
        </div>
    )
}