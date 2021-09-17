// SPDX-License-Identifier: MIT
 pragma solidity ^0.8.0;

contract TodoList {

  uint public taskCount = 0;
  mapping(uint => Task) public tasks;

  struct Task {
    uint id;
    string content;
    bool completed;
  }

  event TaskCreated(
    uint id,
    string content,
    bool completed
  );

  event TaskToogleCompleted(
    uint id,
    bool completed
  );

  constructor() public {
    addTask('hello world');
  }

  function addTask(string memory _content) public {
    tasks[taskCount] = Task(taskCount, _content, false);
    
    emit TaskCreated(taskCount, _content, false);

    taskCount++;
  }

  function getTasks() public view returns (Task[] memory){
    Task[] memory list = new Task[](taskCount);
    for(uint i = 0; i < taskCount; i++) {
      list[i] = tasks[i];
    }

    return list;
  }

  function toogleCompleted(uint _id) public {
    Task storage task = tasks[_id];
    task.completed = !task.completed;

    emit TaskToogleCompleted(task.id, task.completed);
  }
}
