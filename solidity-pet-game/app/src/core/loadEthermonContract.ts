import Web3 from "web3";
import EthermonABI from '../contracts/Ethermon.json';

export const loadEthermonContract = async (web3: Web3) => {
  if (!web3) return;
  const networkId = await web3.eth.net.getId();
  const ethermonABI = EthermonABI as any;

  const netwkorData = ethermonABI.networks[networkId];
  if (netwkorData) {
    return new web3.eth.Contract(ethermonABI.abi, netwkorData.address)
  }

  return undefined;
};