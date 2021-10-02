import { useEffect, useState } from "react";
import Web3 from "web3"

declare const window: any;

export const useWeb3 = () => {
    const [web3, setWeb3] = useState<Web3| undefined>(undefined);

    useEffect(() => {
        const load = async () => {
            if (window.ethereum) {
                const web3 = new Web3(window.ethereum);
                await window.ethereum.enable();

                setWeb3(web3);
            } else if (window.web3) {
                const web3 = new Web3(window.web3.currentProvider);

                setWeb3(web3);
            } else {
                console.log('No ethereum browser detected')
            }
        }
        load()
    }, []);

    return web3;
};
