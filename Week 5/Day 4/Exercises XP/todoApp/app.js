import { TodoList } from './todo.js';

const todo = new TodoList();
todo.addTask("Learn Node.js");
todo.addTask("Build a todo app");
todo.completeTask(0);

console.log(todo.listTasks());
