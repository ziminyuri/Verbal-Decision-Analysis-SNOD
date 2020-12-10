import React from "react";

export const HistoryAnswer = ({history}) => {
    if (!history) {
        return <p className="center">Ответов пока нет</p>
    }

    return (
        <>
            <table className="highlight">
                <thead>
                <tr>
                    <th>№</th>
                    <th>Вопрос</th>
                    <th>Пара альтернатив</th>
                    <th>Ответ</th>
                </tr>
                </thead>

                <tbody>
                {history.map((model, index) => {
                    return (
                        <tr key={index}>
                            <td>{index + 1}</td>
                            <td>{model.question}</td>
                            <td>{model.pair}</td>
                            <td>{model.answer}</td>

                        </tr>
                    )
                })}

                </tbody>
            </table>
        </>
    )
}