import React from "react";

export const Table = ({model}) => {
    if (!model.model_data) {
        return <p className="center">Данные отсутсвуют</p>
    }

    return (
        <>
            <table className="highlight">
                <thead>
                    <tr>
                        {model.model_header.map((col, index) => {
                            return (
                            <th>{col}</th>
                            )
                        })}
                    </tr>
                </thead>

                <tbody>
                {model.model_data.map((row, index) => {
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