import React from "react";
import {HistoryAnswer} from "./HistoryAnswer";
import {ScaleImage} from "./ScaleImage";

export const ModelCard =({model}) =>{
    return(
        <div>
            <h4>Результат</h4>
            <div className="row">
                <div className="col s6 m6">
                    <div className="card blue-grey darken-1">
                        <div className="card-content white-text">
                            <span className="card-title">Лучшая альтернатива по методу ШНУР</span>
                            <p>{model.option_shnur}</p>

                        </div>

                    </div>
                </div>
                <div className="col s6 m6">
                    <div className="card blue-grey darken-1">
                        <div className="card-content white-text">
                            <span className="card-title">Лучшая альтернатива по многокритериальному критерию</span>
                            <p>{model.option_many}</p>
                        </div>
                    </div>
                </div>
            </div>

            <h4>История ответов</h4>
            <HistoryAnswer history={model.history}/>

            <h4>Шкалы Нормализованных Упорядоченных Различий</h4>
            <ScaleImage img={model.img} />
        </div>
    )
}