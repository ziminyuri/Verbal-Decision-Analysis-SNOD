import React from "react";
import {Link} from 'react-router-dom'

export const RangeList = ({models}) => {
    if (!models) {
        return <p className="center">Список для ранжирования модели пуст</p>
    }

    return (
        <>
            <h3>Ранжирование моделей</h3>
            <table className="highlight">
                <thead>
                <tr>
                    <th>Критерий</th>
                    <th>Направление</th>
                    <th>Альтернатива 1</th>
                    <th>Альтернатива 2</th>
                </tr>
                </thead>

                <tbody>
                {models.map((model, index) => {
                    return (
                        <tr key={index}>
                            <td>{model.name}</td>
                            <td>{model.direction}</td>
                            <td>{model.value_1}</td>
                            <td>{model.value_2}</td>
                        </tr>
                    )
                })}

                </tbody>
            </table>
        </>
    )
}