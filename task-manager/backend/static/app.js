const apiStatusDot = document.querySelector("#api-status-dot");
const apiStatusText = document.querySelector("#api-status-text");
const taskForm = document.querySelector("#task-form");
const taskTitle = document.querySelector("#task-title");
const taskDescription = document.querySelector("#task-description");
const taskList = document.querySelector("#task-list");
const taskMessage = document.querySelector("#task-message");
const refreshTasks = document.querySelector("#refresh-tasks");

function setMessage(message) {
  taskMessage.textContent = message;
}

async function requestJson(path, options = {}) {
  const response = await fetch(path, {
    headers: { "Content-Type": "application/json", ...(options.headers || {}) },
    ...options,
  });

  if (!response.ok) {
    const errorBody = await response.json().catch(() => ({ detail: "Request failed" }));
    throw new Error(errorBody.detail || "Request failed");
  }

  if (response.status === 204) {
    return null;
  }

  return response.json();
}

async function checkApiStatus() {
  try {
    const data = await requestJson("/health");
    apiStatusDot.className = "status-dot ok";
    apiStatusText.textContent = data.status;
  } catch (error) {
    apiStatusDot.className = "status-dot error";
    apiStatusText.textContent = "unavailable";
  }
}

function renderTasks(tasks) {
  taskList.replaceChildren();

  if (tasks.length === 0) {
    setMessage("No tasks yet. Create your first task above.");
    return;
  }

  setMessage(`${tasks.length} task${tasks.length === 1 ? "" : "s"} loaded.`);

  for (const task of tasks) {
    const item = document.createElement("li");
    item.className = `task-item${task.completed ? " completed" : ""}`;

    const checkbox = document.createElement("input");
    checkbox.className = "task-checkbox";
    checkbox.type = "checkbox";
    checkbox.checked = task.completed;
    checkbox.setAttribute("aria-label", `Mark ${task.title} as ${task.completed ? "incomplete" : "complete"}`);
    checkbox.addEventListener("change", async () => {
      await updateTask(task, checkbox.checked);
      await loadTasks();
    });

    const content = document.createElement("div");
    const title = document.createElement("p");
    title.className = "task-title";
    title.textContent = task.title;
    const description = document.createElement("p");
    description.className = "task-description";
    description.textContent = task.description || "No description provided.";
    content.append(title, description);

    const actions = document.createElement("div");
    actions.className = "task-actions";
    const deleteButton = document.createElement("button");
    deleteButton.className = "danger";
    deleteButton.type = "button";
    deleteButton.textContent = "Delete";
    deleteButton.addEventListener("click", async () => {
      await requestJson(`/tasks/${task.id}`, { method: "DELETE" });
      await loadTasks();
    });
    actions.append(deleteButton);

    item.append(checkbox, content, actions);
    taskList.append(item);
  }
}

async function loadTasks() {
  try {
    const tasks = await requestJson("/tasks");
    renderTasks(tasks);
  } catch (error) {
    setMessage(error.message);
  }
}

async function updateTask(task, completed) {
  await requestJson(`/tasks/${task.id}`, {
    method: "PUT",
    body: JSON.stringify({
      title: task.title,
      description: task.description,
      completed,
    }),
  });
}

taskForm.addEventListener("submit", async (event) => {
  event.preventDefault();

  const title = taskTitle.value.trim();
  const description = taskDescription.value.trim();

  if (!title) {
    setMessage("Task title is required.");
    taskTitle.focus();
    return;
  }

  try {
    await requestJson("/tasks", {
      method: "POST",
      body: JSON.stringify({ title, description: description || null, completed: false }),
    });
    taskForm.reset();
    taskTitle.focus();
    await loadTasks();
  } catch (error) {
    setMessage(error.message);
  }
});

refreshTasks.addEventListener("click", loadTasks);

checkApiStatus();
loadTasks();
