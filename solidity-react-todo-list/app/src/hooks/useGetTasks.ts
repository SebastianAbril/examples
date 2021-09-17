import { useEffect, useState } from "react";

export const useGetTasks = (todoListContract: any | undefined) => {
    const [tasks, setTasks] = useState([]);

    const getTasks = async () => {
        if (!todoListContract) return;

        const tasks = await todoListContract.methods.getTasks().call();
        setTasks(tasks);
    };
    
    useEffect(() => {
        getTasks();
    }, [todoListContract]);


    return { tasks, getTasks };
};