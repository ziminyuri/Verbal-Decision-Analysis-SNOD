import React from 'react';
import {BrowserRouter as Router} from 'react-router-dom'
import 'materialize-css'
import {useRoutes} from './routes'
import {useAuth} from './hooks/auth.hooks'
import {AuthContext} from './context/AuthContext'
import {Navbar} from "./components/Navbar";



function App() {
    const {login, logout, token, userId} = useAuth()
    const isAuthendificated = !!token
  const routes = useRoutes(isAuthendificated)
  return (
      <AuthContext.Provider value={{
            token, login, logout, userId, isAuthendificated
      }}>

          <Router>
              {isAuthendificated && <Navbar/>}
            <div className="container">
                {routes}
            </div>
          </Router>
      </AuthContext.Provider>
  );
}

export default App;
