import React, {useCallback, useEffect, useState} from "react";
import {useHttp} from "../hooks/http.hook";
import {RangeList} from "../components/RangeList";
import {useHistory} from "react-router-dom";

export const RangePage = () => {
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
            const fetched = await request('http://127.0.0.1:8000/api/v1/model/demo/park/create',
                'GET', null)
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
            {!loading && <RangeList models={models}/>}
            <div className='row'>

            </div>
            <button className="waves-effect waves-light btn btn-custom" onClick={mainPageHandler}>
                <i className="material-icons left">backspace</i>На главную</button>
        </>
    )
}