import { useEffect } from "react";

export const useListenEvents = (todoListContract: any | undefined, getTasks: () => void)  => {
    useEffect(() => {
        if(!todoListContract) return;
    
        todoListContract.events.TaskCreated({}).on('data', (event: any) => {
          console.log('new task')
          getTasks();
        });
    
        todoListContract.events.TaskToogleCompleted({}).on('data', (event: any) => {
          console.log('TaskToogleCompleted')
          getTasks();
        });
    
      }, [todoListContract, getTasks]);
};