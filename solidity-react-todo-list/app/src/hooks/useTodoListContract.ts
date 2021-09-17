import { useEffect, useState } from 'react';
import Web3 from 'web3';
import TodoList from '../contracts/TodoList.json';

export const useTodoListContract = (web3: Web3 | undefined) => {
    const [contract, setContract] = useState<any>();

    useEffect(() => {
        const loadContract = async () => {
            if (!web3) return;
            const networkId = await web3.eth.net.getId();
            const TodoListContract = TodoList as any; 

            const netwkorData = TodoListContract.networks[networkId];
            if (netwkorData) {
                setContract(
                  new web3.eth.Contract(TodoListContract.abi, netwkorData.address)
                );
            }
        };

        loadContract();
    }, [web3]);

    return contract;
};