import React, {useCallback, useEffect, useState} from "react";
import {useParams} from 'react-router-dom'
import {useHttp} from "../hooks/http.hook";
import {ModelCard} from "../components/ModelCard";
import {Loader} from "../components/Loader";


export const ResultModelPage =() => {
    const {request, loading} = useHttp()
    const [model, setModel] = useState('')
    const modelId = useParams().id

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
        </>
    )
}