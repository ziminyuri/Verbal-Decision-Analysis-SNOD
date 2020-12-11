import React from "react";

export const ScaleImage = ({img}) => {
    if (!img) {
        return <p className="center">Критериев слишком много</p>
    }

    return (
        <>
            <table className="highlight">
                <thead>
                <tr>
                    <th>№</th>
                    <th>Пара альтернатив</th>
                    <th>ШНУР</th>
                </tr>
                </thead>

                <tbody>
                {img.map((img, index) => {
                    return (
                        <tr key={index}>
                            <td>{index + 1}</td>
                            <td>{img.pair}</td>
                            <td>
                                <img src={img.path}/>
                            </td>
                        </tr>
                    )
                })}

                </tbody>
            </table>
        </>
    )
}