import React from 'react';
import './App.css';
import {AppContext, AppContextType} from './app/AppContext';
import HomeScreen from "./app/screens/HomeScreen";
import {Provider} from "./core/Provider";

function App() {
    const appContext: AppContextType = {
        provider: new Provider()
    };

    return (
        <div className="App">
            <AppContext.Provider value={appContext}>
                <HomeScreen/>
            </AppContext.Provider>
        </div>
    );
}

export default App;
