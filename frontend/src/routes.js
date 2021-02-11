import React from "react";
import {Switch, Route, Redirect} from "react-router-dom"
import {InputDataPage} from './pages/InputDataPage'
import {QuestionPage} from './pages/QuestionPage'
import {IndexPage} from './pages/IndexPage'
import {DemoModelPage} from './pages/DemoModelPage'
import {AuthPage} from "./pages/AuthPage";
import {CreateModelPage} from "./pages/CreateModelPage";
import {ResultModelPage} from "./pages/ResultModelPage"
import {ModelsPage} from "./pages/ModelsPage";
import {RangePage} from "./pages/RangePage";


export const useRoutes = isAuthentificated =>{
    if (isAuthentificated) {
        return (
            <Switch>
                <Route path="/" exact>
                    <IndexPage/>
                </Route>
                <Route path="/model/create" exact>
                    <CreateModelPage/>
                </Route>
                <Route path="/input_data" exact>
                    <InputDataPage/>
                </Route>

                {/* ШНУР */}
                <Route path="/model/demo/question" exact>
                    <QuestionPage/>
                </Route>

                {/* ПАРК */}
                <Route path="/model/demo/question/park" exact>
                    <RangePage/>
                </Route>


                <Route path="/model/demo" exact>
                    <DemoModelPage/>
                </Route>
                <Route path="/model/result/:id">
                    <ResultModelPage/>
                </Route>
                <Route path="/models">
                    <ModelsPage/>
                </Route>
            </Switch>
        )
    }
    return(
        <Switch>
            <Route path="/" exact>
                <AuthPage/>
            </Route>
            <Redirect to={"/"}/>
        </Switch>
    )
}