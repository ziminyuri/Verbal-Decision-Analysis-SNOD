import React from "react";

export const TableWinners = ({model}) => {
    if (!model.winners_data) {
        return <p className="center">Данные отсутсвуют</p>
    }

    return (
        <>
            <table className="highlight">
                <thead>
                <tr>
                    <th>№ Пары</th>
                    {model.winners_header.map((col, index) => {
                        return (
                            <th key={index}>{col}</th>
                        )
                    })}
                </tr>
                </thead>

                <tbody>
                {model.winners_data.map((row, index) => {
                    return (
                        <tr key={index}>
                            <td>{index + 1}</td>
                            {row.map((col, index1) => {
                                return (
                                    <td key={index1}>{col}</td>
                                )
                            })}
                        </tr>
                    )
                })}

                </tbody>
            </table>
        </>
    )
}