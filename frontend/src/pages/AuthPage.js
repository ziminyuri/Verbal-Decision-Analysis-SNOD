import React, {useState, useEffect, useContext} from "react";
import {useHttp} from "../hooks/http.hook";
import {useMessage} from '../hooks/error.hook'
import {AuthContext} from "../context/AuthContext";

export const AuthPage =() => {
    const auth = useContext(AuthContext)
    const message = useMessage()
    const {loading, request, error, clearError} = useHttp()
    const [authForm, setAuthForm] = useState ({
        email: '', password: ''
    })

    useEffect(() => {
        message(error)
        clearError()
    }, [error, message, clearError])

    const changeHandler = event => {
        setAuthForm({...authForm, [event.target.name]: event.target.value })           // работаем с оператором spred
    }

    const registerHandler = async () => {
        try {
            const data = await request('http://127.0.0.1:8000/api/v1/registration', 'POST', {...authForm})
            console.log(data)
        } catch (e) {}
    }

    const loginHandler = async () => {
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
                    <div className="card-content white-text">
                        <span className="card-title auth-logo-custom">Авторизация</span>
                        <div className="input-field">
                            <input
                                id="email"
                                type="text"
                                className="validate"
                                name="email"
                                value={authForm.email}
                                onChange={changeHandler}
                            />
                                <label htmlFor="email">E-mail</label>
                        </div>

                        <div className="input-field">
                        <input
                            id="password"
                            type="password"
                            className="validate"
                            name="password"
                            value={authForm.password}
                            onChange={changeHandler}
                        />
                        <label htmlFor="password">Пароль</label>
                    </div>

                    </div>
                    <div className="card-action">
                        <button
                            className="btn auth-btn-custom"
                            disabled={loading}
                            onClick={loginHandler}
                        >Войти</button>
                        <button
                            className="btn auth-btn-custom"
                            onClick={registerHandler}
                            disabled={loading}            // Если загрузка пошла, то выключить кнопку
                        >Регистрация</button>
                    </div>
                </div>
            </div>
        </div>
    )
}