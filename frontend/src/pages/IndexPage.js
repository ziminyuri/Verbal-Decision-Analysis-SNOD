import React from "react";
import {NavLink, useHistory} from 'react-router-dom'
import {useHttp} from "../hooks/http.hook";


export const IndexPage =() => {
    const {request} = useHttp()
    const history = useHistory()


    const useDemoModelHandler = async () => {
        try {
            history.push('/model/demo/question')
        } catch (e) {}
    }

    return (
        <div>
            <h4>Главная страница</h4>
            <div className="row">
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