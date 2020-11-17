import React, {useEffect, useState} from "react";
import {useHttp} from "../hooks/http.hook";

export const QuestionPage =() => {
    const {loading, request} = useHttp()
    const [response, setResponse] = useState ('')

    // Зибраем данные объектов с сервера при загрузки страницы
    useEffect(() => {

        const fetchData = async () => {
            const data = await request('http://127.0.0.1:8000/api/v1/model/demo/create', 'GET', )
            console.log(data)
            setResponse(data);
        };

        fetchData();
    }, []);

    const questionHandler = async () => {
        try {
            const data = await request('api/v1/question', 'POST', {})
            console.log('Data', data)
        }
        catch (e) {}
    }
    return (
        <div>
            <h3>Ответьте на вопрос:</h3>

            <div className="row">
                <div className="col s12">
                    <div className="card blue-grey darken-1">
                        <div className="card-content white-text">
                            <span className="card-title">{response.question}</span>
                        </div>
                        <div className="card-action">
                            <button
                                onClick={questionHandler}
                                disabled={loading}
                            >Важнее</button>
                            <button
                                onClick={questionHandler}
                                disabled={loading}
                            >Нет, не важнее</button>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    )
}

