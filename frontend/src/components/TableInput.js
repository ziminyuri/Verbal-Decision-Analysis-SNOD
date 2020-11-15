import React, {useEffect, useState} from "react";
import {SettingsModel} from "../components/SettingsModel";

export const TableInput = (props) => {
    const alternative = props.alternative
    const criteria = props.criteria

    return (
        <div>
            <p>Table</p>

            <table>
                <thead>
                <tr>
                    <th>Критерии</th>
                    <th>Направления</th>
                    <th>Item Price</th>
                </tr>
                </thead>

                <tbody>
                <tr>
                    <td>Alvin</td>
                    <td>Eclair</td>
                    <td>$0.87</td>
                </tr>

                </tbody>
            </table>

        </div>
    );
};
