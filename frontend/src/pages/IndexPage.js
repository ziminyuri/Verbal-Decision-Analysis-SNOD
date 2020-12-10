import React from "react";
import {NavLink, useHistory} from 'react-router-dom'
//import {useHttp} from "../hooks/http.hook";


export const IndexPage =() => {
    //const {} = useHttp()
    const history = useHistory()


    const useDemoModelHandler = async () => {
        try {
            history.push('/model/demo/question')
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
                                <input type="file" name="file" />
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
                                <a
                                onClick={useDemoModelHandler}>Использовать</a>
                            </div>
                        </div>
            </div>
            </div>
        </div>
    )
}