import React, {useEffect, useState} from "react";


export const CreateModelPage = () => {
    const optionValue = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    useEffect(() => {
        var elems1 = document.getElementById("sel1");
        var elems2 = document.getElementById("sel2");
        var instances1 = window.M.FormSelect.init(elems1, {});
        var instances2 = window.M.FormSelect.init(elems2, {});
    }, []);

    useEffect(() =>{
        window.M.updateTextFields()
    }, [])

    const [alternative, setAlternative] = useState(1)
    const [criteria, setCriteria] = useState(1)
    const [flagInputData, setFlagInputData] = useState (false)


    const inputDataHandler = () => {
        console.log('сравпып')
        console.log(criteria)
        setFlagInputData(true)

    }
    function ShowingContent(){
        if (flagInputData) {
            return (<p> Таблица</p>)
        }
        else{
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
                                onClick={inputDataHandler}

                            >Далее</button>
                            <button className='btn auth-btn-custom'>Назад</button>
                        </div>
                    </div>
                </div>
            </div>
            )
        }
    }

    return (
        <ShowingContent/>
    );
};

