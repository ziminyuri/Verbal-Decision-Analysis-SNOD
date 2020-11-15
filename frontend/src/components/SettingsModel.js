import React, {useEffect, useState} from "react";
import {useHistory} from "react-router-dom";

export const SettingsModel = (props) => {
    const history = useHistory()

    const previousPageHandler = event => {
        event.preventDefault()
        history.push('/')
    }

    const optionValue = [2, 3, 4, 5, 6, 7, 8, 9, 10]

    useEffect(() => {
        var elems1 = document.getElementById("sel1");
        var elems2 = document.getElementById("sel2");
        var instances1 = window.M.FormSelect.init(elems1, {});
        var instances2 = window.M.FormSelect.init(elems2, {});
    }, []);

    const [alternative, setAlternative] = useState(1)
    const [criteria, setCriteria] = useState(1)

    return (
        <div className="row">
            <div className="col s6 offset-s3">
                <div className="card blue-grey lighten-5">
                    <div className="card-content">
                        <div className="input-field">
                            <select id="sel1" value={alternative} name="alternative" onChange={e => setAlternative(e.target.value)}>
                                {optionValue.map(v => (
                                    <option key={v} value={v} >Альтернатив: {v}</option>
                                ))}

                            </select>

                            <label>Кол-во альтернатив</label>
                        </div>

                        <div className="input-field">
                            <select id="sel2" value={criteria} name="criteria" onChange={e => setCriteria(e.target.value)}>



                                {optionValue.map(v => (
                                    <option key={v} value={v}>Критериев: {v}</option>
                                ))}

                            </select>
                            <label>Кол-во критериев</label>
                        </div>
                    </div>
                    <div className="card-action">
                        <button
                            className='btn auth-btn-custom'
                            onClick={()=>props.setNext(true, alternative, criteria)}

                        >Далее</button>
                        <button
                            className='btn auth-btn-custom'
                            onClick={previousPageHandler}
                        >Назад</button>
                    </div>
                </div>
            </div>
        </div>
    )
}