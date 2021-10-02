import Web3 from "web3";

export const getAccount = async (web3: Web3) => {
    const accounts = await web3.eth.getAccounts();
    return accounts[0];
}