import React from "react";
import {Switch, Route, Redirect} from "react-router-dom"
import {InputDataPage} from './pages/InputDataPage'
import {QuestionPage} from './pages/QuestionPage'
import {IndexPage} from './pages/IndexPage'
import {TablePage} from './pages/TablePage'
import {AuthPage} from "./pages/AuthPage";


export const useRoutes =() =>{
    return(
        <Switch>
            <Route path="/" exact>
                <IndexPage/>
            </Route>
            <Route path="/auth" exact>
                <AuthPage/>
            </Route>
            <Route path="/input_data" exact>
                <InputDataPage/>
            </Route>
            <Route path="/question" exact>
                <QuestionPage/>
            </Route>
            <Route path="/data" exact>
                <TablePage/>
            </Route>
            <Redirect to={"/"}/>
        </Switch>
    )
}