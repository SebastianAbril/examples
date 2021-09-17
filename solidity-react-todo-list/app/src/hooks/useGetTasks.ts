import { useCallback, useEffect, useState } from "react";

export const useGetTasks = (todoListContract: any | undefined) => {
    const [tasks, setTasks] = useState([]);

    const getTasks = useCallback(async() => {
        if (!todoListContract) return;

        const tasks = await todoListContract.methods.getTasks().call();
        setTasks(tasks);
      }, [setTasks, todoListContract]);
    
    useEffect(() => {
        getTasks();
    }, [todoListContract, getTasks]);

    return { tasks, getTasks };
};