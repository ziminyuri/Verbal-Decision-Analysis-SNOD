import React, {useCallback, useEffect, useState} from "react";
import {useHistory, useParams} from 'react-router-dom'
import {useHttp} from "../hooks/http.hook";
import {ModelCard} from "../components/ModelCard";
import {Loader} from "../components/Loader";
import { Redirect } from 'react-router'


export const ResultModelPage =() => {
    const {request, loading} = useHttp()
    const [model, setModel] = useState('')
    const modelId = useParams().id
    const history = useHistory()

    const mainPageHandler = async () => {
        try {
            history.push('/')
        } catch (e) {}
    }

    const modelsPageHandler = async () => {
        try {
            history.push('/models')
        } catch (e) {}
    }



    const getModel = useCallback(async ()=>{
        try{
            const fetched = await request(`http://127.0.0.1:8000/api/v1/model/result/${modelId}`)
            setModel(fetched)
        }

        catch (e) {
            
        }
    },[request, modelId])

    useEffect(()=>{
        getModel()
    },[getModel])

    if (loading) return ( <div>
        <Loader />
    </div>)

    return (
        <>
            {! loading && <ModelCard model={model}/>}
                <div className='row'>
            <div className="col 1">
            <button className="waves-effect waves-light btn" onClick={mainPageHandler}>
                <i className="material-icons left">backspace</i>
                На главную</button>
            </div>
            <div className="col 1">
            <button className="waves-effect waves-light btn btn-custom" onClick={modelsPageHandler}>
                <i className="material-icons right">list</i>К моделям</button>
            </div>
                </div>
        </>
    )
}