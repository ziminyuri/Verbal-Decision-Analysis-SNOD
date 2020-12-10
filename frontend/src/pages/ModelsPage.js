import React, {useCallback, useContext, useEffect, useState} from "react";
import {useHttp} from "../hooks/http.hook";
import {AuthContext} from "../context/AuthContext";
import {ModelsList} from "../components/ModelsList";

export const ModelsPage = () => {
    const [models, setModels] = useState(null)
    const {loading, request} = useHttp()
    const {token} = useContext(AuthContext)

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
        </>
    )
}