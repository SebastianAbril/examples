const TodoList = artifacts.require('TodoList');

contract('TodoListShould', function (/* accounts */) {

  let todoList;

  before(async() => {
    todoList = await TodoList.new();
  });

  it('deploys successfully', async () => {
    const address = await todoList.address;

    assert.notEqual(address, 0x0);
    assert.notEqual(address, '');
    assert.notEqual(address, null);
    assert.notEqual(address, undefined);
  });

  it('add a first demo task', async () => {
    const task = await todoList.tasks(0);

    assert.equal(task.id, 0);
    assert.equal(task.content, 'hello world');
    assert.equal(task.completed, false);
  });

  it('get all the tasks', async () => {
    const tasks = await todoList.getTasks();

    assert.equal(tasks.length, 1);
    assert.equal(tasks[0].id, 0);
    assert.equal(tasks[0].content, 'hello world');
    assert.equal(tasks[0].completed, false);
  });

  it('add a new task', async () => {
    const result = await todoList.addTask('hello ETH');

    const taskCount = await todoList.taskCount();
    assert.equal(taskCount.toNumber(), 2);

    const task = await todoList.tasks(1);
    assert.equal(task.id, 1);
    assert.equal(task.content, 'hello ETH');
    assert.equal(task.completed, false);

    const event = result.logs[0].args;
    assert.equal(event.id, 1);
    assert.equal(event.content, 'hello ETH');
    assert.equal(event.completed, false);
  });

  it('toogle a task', async () => {
    const result = await todoList.toogleCompleted(0);

    const task = await todoList.tasks(0);
    assert.equal(task.id, 0);
    assert.equal(task.content, 'hello world');
    assert.equal(task.completed, true);

    const event = result.logs[0].args;
    assert.equal(event.id, 0);
    assert.equal(event.completed, true);
  });

});
