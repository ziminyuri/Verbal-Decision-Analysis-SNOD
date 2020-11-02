import React from "react";
import {useHttp} from "../hooks/http.hook";

export const QuestionPage =() => {
    const {loading, request} = useHttp()
    const questionHandler = async () => {
        try {
            const data = await request('api/v1/question', 'POST', {})
            console.log('Data', data)
        }
        catch (e) {}
    }
    return (
        <div>
            <h1>Страница где задаются вопросых</h1>

            <div className="row">
                <div className="col s12">
                    <div className="card blue-grey darken-1">
                        <div className="card-content white-text">
                            <span className="card-title">Card Title</span>
                            <p>Здесь указывается вопрос</p>
                        </div>
                        <div className="card-action">
                            <button
                                onClick={questionHandler}
                                disabled={loading}
                            >Вариант 1</button>
                            <button
                                onClick={questionHandler}
                                disabled={loading}
                            >Вариант 2</button>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    )
}

