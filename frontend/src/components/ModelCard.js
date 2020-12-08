import React from "react";

export const ModelCard =({model}) =>{
    return(
        <div>
            <h1>Результат</h1>
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
        </div>
    )
}