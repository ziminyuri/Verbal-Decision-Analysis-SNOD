import React, {useEffect, useState} from "react";
import {SettingsModel} from "../components/SettingsModel";
import {TableInput} from "../components/TableInput";

export const CreateModelPage = () => {

    const [flagInputData, setFlagInputData] = useState (false)
    const [alternative, setAlternative] = useState(1)
    const [criteria, setCriteria] = useState(1)

    const inputDataHandler = (flag, alternative, criteria) => {
        setAlternative(alternative)
        setCriteria(criteria)
        setFlagInputData(flag)
    }

    return (
        <div>
        {flagInputData ? <TableInput props={{alternative, criteria}}/> : <SettingsModel setNext={inputDataHandler}/>}
        </div>

    );
};

