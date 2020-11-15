import React from "react";
import {NavLink} from 'react-router-dom'

export const DemoModelPage =() => {

    const table_items = [
        {id: 1, direction: 'max', variant_1: 400, variant_2: 300, variant_3: 250, variant_4: 150 },
        {id: 2, direction: 'min', variant_1: 1, variant_2: 5, variant_3: 3, variant_4: 5 }
    ]


    return (
        <div>

            <h1>Страница демо данных</h1>
            <table className="highlight">
                <thead>
                <tr>
                    <th>Критерий</th>
                    <th>Направление</th>
                    <th>Вариант 1</th>
                    <th>Вариант 2</th>
                    <th>Вариант 3</th>
                    <th>Вариант 4</th>
                </tr>
                </thead>

                <tbody>
                { table_items.map(item => {
                    return (
                    <tr>
                        <td>{ item.id }</td>
                        <td>{ item.direction }</td>
                        <td>{ item.variant_1 }</td>
                        <td>{ item.variant_2 }</td>
                        <td>{ item.variant_3 }</td>
                        <td>{ item.variant_4 }</td>
                    </tr>
                    )
                    }) }
                </tbody>
            </table>

            <NavLink to="/question" className="waves-effect waves-light btn">
                <i className="material-icons left">cloud</i>Перейти к опросу для определения лучшей альтернатив</NavLink>
        </div>

    )
}