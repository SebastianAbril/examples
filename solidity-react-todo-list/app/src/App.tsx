import React, { useEffect, useState } from 'react';
import './App.css';
import { useWeb3 } from './hooks/useWeb3';
import { useTodoListContract } from './hooks/useTodoListContract';
import { useGetTasks } from './hooks/useGetTasks';

function App() {
  const web3 = useWeb3();
  const todoListContract = useTodoListContract(web3);
  const {tasks, getTasks} = useGetTasks(todoListContract);
  const [taskName, setTaskName] = useState<string>('');

  const onSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!web3) return;
    const accounts = await web3.eth.getAccounts();
    await todoListContract.methods
      .addTask(taskName)
      .send({from: accounts[0]});

    await getTasks();

    setTaskName('');
  };

  const onToogleTask = async (id: string) => {
    if (!web3) return;

    const accounts = await web3.eth.getAccounts();
    await todoListContract.methods
      .toogleCompleted(id)
      .send({from: accounts[0]});

    await getTasks();
  };


  return (
    <div className="App">
      <h1>Simple ETH-TODO-LIST</h1>
      <form onSubmit={onSubmit}>
        <input type="text" value={taskName} onChange={(e) => setTaskName(e.target.value)}/>
      </form>
      <ul className="list">
        {tasks.map((task: any) => {
          return <li key={task.id}><input type="checkbox" onChange={() => onToogleTask(task.id)} checked={task.completed} />{task.content}</li>
          })}
      </ul>
    </div>
  );
}

export default App;
