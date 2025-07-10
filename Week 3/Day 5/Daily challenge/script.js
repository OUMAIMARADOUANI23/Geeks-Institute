  function addTask() {
      const input = document.getElementById("task-input");
      const taskText = input.value.trim();
      if (taskText === "") return;

      const taskItem = document.createElement("div");
      taskItem.className = "task-item";

      const deleteBtn = document.createElement("button");
      deleteBtn.className = "delete-btn";
      deleteBtn.textContent = "❌";
      deleteBtn.onclick = () => taskItem.remove();

      const checkbox = document.createElement("input");
      checkbox.type = "checkbox";
      checkbox.onchange = () => {
        if (checkbox.checked) {
          label.style.textDecoration = "line-through";
          label.style.color = "red";
        } else {
          label.style.textDecoration = "none";
          label.style.color = "#333";
        }
      };

      const label = document.createElement("label");
      label.textContent = taskText;

      taskItem.appendChild(deleteBtn);
      taskItem.appendChild(checkbox);
      taskItem.appendChild(label);

      document.getElementById("todo-container").appendChild(taskItem);
      input.value = "";
    }

    function clearTasks() {
      document.getElementById("todo-container").innerHTML = "";
    }