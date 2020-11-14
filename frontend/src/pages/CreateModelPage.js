import React, { useEffect } from "react";


export const CreateModelPage = (props) => {
    const optionValue = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    useEffect(() => {
        var elems1 = document.getElementById("sel1");
        var elems2 = document.getElementById("sel2");
        var instances1 = window.M.FormSelect.init(elems1, {});
        var instances2 = window.M.FormSelect.init(elems2, {});
    }, []);

    const inputDataHandler = async () => {
        try {
            const data = await request('http://127.0.0.1:8000/api/v1/login', 'POST', {...authForm})
            auth.login(data.token, data.user_id)
            console.log(data)
        } catch (e) {}
    }

    return (
        <div className="row">
            <div className="col s6 offset-s3">
                <div className="card blue-grey lighten-5">
                    <div className="card-content">
                        <div className="input-field">
                            <select id="sel1">
                                <option value="" disabled selected>
                                    Выберите кол-во
                                </option>

                                {optionValue.map(v => (
                                    <option value={v}>Альтернатив: {v}</option>
                                ))}

                            </select>
                            <label>Кол-во альтернатив</label>
                        </div>

                        <div className="input-field">
                            <select id="sel2">
                                <option value="" disabled selected>
                                    Выберите кол-во
                                </option>

                                {optionValue.map(v => (
                                    <option value={v}>Критериев: {v}</option>
                                ))}

                            </select>
                            <label>Кол-во критериев</label>
                        </div>
                    </div>
                    <div className="card-action">
                        <button
                            className='btn auth-btn-custom'
                            onClick={inputDatahandler}
                        >Далее</button>
                        <button className='btn auth-btn-custom'>Назад</button>
                    </div>
                </div>
            </div>
        </div>
    );
};

