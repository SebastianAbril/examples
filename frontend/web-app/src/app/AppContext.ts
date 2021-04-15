import React from 'react';
import {Provider} from "../core/Provider";

export type AppContextType = {
    provider: Provider;
}
export const AppContext = React.createContext<AppContextType>({
    provider: new Provider()
});
