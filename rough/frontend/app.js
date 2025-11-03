// ====== Selectors ======
const taskInput = document.querySelector('.task-input');
const taskDescInput = document.querySelector('.task-desc-input');
const taskButton = document.querySelector('.task-button');
const taskList = document.querySelector('.task-list');
const filterByStatus = document.querySelector('.filter-tasks');
const sortByPriority = document.querySelector('.sort-tasks');

// ====== Event Listeners ======
taskButton.addEventListener('click', addTask);
taskList.addEventListener('click', handleTaskClick);
filterByStatus.addEventListener('change', filterStatus);
sortByPriority.addEventListener('change', sortPriority);

// ====== Functions ======
function addTask(event) {
    event.preventDefault();
    if(!taskInput.value.trim()) return;

    // Task container
    const taskDiv = document.createElement('div');
    taskDiv.classList.add('task');

    // Task title
    const newTask = document.createElement('li');
    newTask.innerText = taskInput.value;
    newTask.classList.add('task-item');
    taskDiv.appendChild(newTask);

    // Task description
    const newDesc = document.createElement('p');
    newDesc.innerText = taskDescInput.value;
    newDesc.classList.add('task-desc');
    taskDiv.appendChild(newDesc);

    // Button container
    const buttonContainer = document.createElement('div');
    buttonContainer.classList.add('task-buttons');

    // Completed button
    const completedButton = document.createElement('button');
    completedButton.innerHTML = '<i class="fas fa-check"></i>';
    completedButton.classList.add('complete-btn');
    buttonContainer.appendChild(completedButton);

    // Priority button
    const priorityButton = document.createElement('button');
    priorityButton.innerHTML = '🔵 Low';
    priorityButton.dataset.priority = 1;
    priorityButton.classList.add('priority-status');
    priorityButton.addEventListener('click', () => {
        let current = parseInt(priorityButton.dataset.priority);
        let next = (current % 3) + 1;
        priorityButton.dataset.priority = next;

        if(next === 1) priorityButton.innerHTML = '🔵 Low';
        else if(next === 2) priorityButton.innerHTML = '🟠 Medium';
        else priorityButton.innerHTML = '🔴 High';
    });
    buttonContainer.appendChild(priorityButton);

    // Delete button
    const deleteButton = document.createElement('button');
    deleteButton.innerHTML = '<i class="fas fa-trash"></i>';
    deleteButton.classList.add('trash-btn');
    buttonContainer.appendChild(deleteButton);

    // Append buttons to task
    taskDiv.appendChild(buttonContainer);

    // Append task
    taskList.appendChild(taskDiv);

    // Inside addTask, after appending taskDiv
    taskDiv.addEventListener('click', (e) => {
        // Avoid toggling when clicking buttons
        if(e.target.closest('button')) return;
        taskDiv.classList.toggle('show-desc');
    });


    // Clear inputs
    taskInput.value = '';
    taskDescInput.value = '';
}

// Handles click events for delete and complete buttons
function handleTaskClick(e) {
    const task = e.target.closest('.task');
    if(!task) return;

    // Delete button
    if(e.target.closest('.trash-btn')) {
        task.classList.add('fall');
        task.addEventListener('transitionend', () => task.remove());
    }

    // Complete button
    if(e.target.closest('.complete-btn')) {
        task.classList.toggle('completed');
    }
}

// Filter tasks by status
function filterStatus(e) {
    const tasks = taskList.childNodes;
    tasks.forEach(task => {
        if(task.nodeType !== 1) return;
        switch(e.target.value) {
            case 'all':
                task.style.display = 'flex';
                break;
            case 'completed':
                task.style.display = task.classList.contains('completed') ? 'flex' : 'none';
                break;
            case 'pending':
                task.style.display = !task.classList.contains('completed') ? 'flex' : 'none';
                break;
        }
    });
}

function sortPriority(e) {
    const tasks = Array.from(taskList.children);
    tasks.sort((a, b) => {
        const pA = parseInt(a.querySelector('.priority-status').dataset.priority);
        const pB = parseInt(b.querySelector('.priority-status').dataset.priority);
        return pB - pA;
    });
    tasks.forEach(task => taskList.appendChild(task));
}
