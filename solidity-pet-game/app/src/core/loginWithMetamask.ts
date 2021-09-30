import Web3 from "web3";

declare const window: any;

export const loginWithMetamask = async (): Promise<Web3|undefined> => {
    if (window.ethereum) {
        const web3 = new Web3(window.ethereum);
        await window.ethereum.enable();

        return web3;
    } else if (window.web3) {
        const web3 = new Web3(window.web3.currentProvider);
        return web3;
    } else {
        return undefined;
    }
}