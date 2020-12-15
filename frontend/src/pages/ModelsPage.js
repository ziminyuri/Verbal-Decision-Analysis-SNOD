import React, {useCallback, useEffect, useState} from "react";
import {useHttp} from "../hooks/http.hook";
import {ModelsList} from "../components/ModelsList";
import {useHistory} from "react-router-dom";

export const ModelsPage = () => {
    const [models, setModels] = useState(null)
    const {loading, request} = useHttp()
    const history = useHistory()

    const mainPageHandler = async () => {
        try {
            history.push('/')
        } catch (e) {}
    }

    const fetchModels = useCallback( async () => {
        try {
            const fetched = await request('http://127.0.0.1:8000/api/v1/models', 'GET', null)
            setModels(fetched)
        }
        catch (e) {}
    }, [request])

    useEffect(()=>{
        fetchModels()
    }, [fetchModels])

    if (loading)
        return (
            <div>
                <h1>Загрузка</h1>
            </div>
        )

    return (
        <>
            {!loading && <ModelsList models={models}/>}
            <div className='row'></div>
            <button className="waves-effect waves-light btn btn-custom" onClick={mainPageHandler}>
                <i className="material-icons left">backspace</i>На главную</button>
        </>
    )
}