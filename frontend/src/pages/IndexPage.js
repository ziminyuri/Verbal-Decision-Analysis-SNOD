import React, {useState} from "react";
import {NavLink, useHistory} from 'react-router-dom'
import {useHttp} from "../hooks/http.hook";
import {Loader} from "../components/Loader";


export const IndexPage =() => {
    const {loading, request} = useHttp()
    const history = useHistory()

    const useDemoModelPARKHandler = async () => {
        try {
            history.push('/model/demo/question/park')
        } catch (e) {}
    }

    const useDemoModelHandler = async () => {
        try {
            history.push('/model/demo/question')
        } catch (e) {}
    }

    const useAutoModelHandler = async () => {
        // Автоматическом режиме
        const model = await request('/api/v1/model/auto/create', 'GET', )
        history.push(`/model/result/${model.model_id}`)
    }

    if (loading) {
        return <Loader />
    }

    else return (
        <div>
            <h4>Главная страница</h4>
            <div className="row">
            <div className="col s6 m6">
                        <div className="card blue-grey darken-1">
                            <div className="card-content white-text">
                                <span className="card-title">Использовать исходные данные</span>
                                <p>Для данной модели предлагается 7 криетриев и 4 альтернативы</p>
                            </div>
                            <div className="card-action">
                                <a
                                    onClick={useDemoModelPARKHandler}>Использовать ПАРК</a>
                                <a
                                onClick={useDemoModelHandler}>Использовать ШНУР</a>
                            </div>
                            <div className="card-action">
                                <a
                                    onClick={useAutoModelHandler}>Автогенерация ШНУР</a>
                            </div>

                        </div>
            </div>
            </div>
        </div>
    )
}