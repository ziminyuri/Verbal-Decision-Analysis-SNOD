import React from "react";
import {Link} from 'react-router-dom'

export const ModelsList = ({models}) => {
    if (!models) {
        return <p className="center">Моделей пока нет</p>
    }

    return (
        <>
            <h3>Модели</h3>
            <table className="highlight">
                <thead>
                <tr>
                    <th>№</th>
                    <th>Название</th>
                    <th>Подробнее</th>
                </tr>
                </thead>

                <tbody>
                {models.map((model) => {
                    return (
                        <tr key={model.id}>
                            <td>{model.id}</td>
                            <td>{model.name}</td>
                            <td>
                                <Link to={`/model/result/${model.id}`} >
                                     Подробнее
                                </Link>
                            </td>
                        </tr>
                    )
                })}

                </tbody>
            </table>
        </>
    )
}