const BASE_URL = "http://127.0.0.1:8000/tasks/";
const AUTH_URL = "http://127.0.0.1:8000/";

// Selectors
const authSection = document.querySelector('.auth-section');
const taskSection = document.querySelector('.task-section');
const loginForm = document.querySelector('.login-form');
const registerForm = document.querySelector('.register-form');
const showRegisterBtn = document.querySelector('.show-register');
const showLoginBtn = document.querySelector('.show-login');
const logoutBtn = document.querySelector('.logout-btn');

const search = document.querySelector('.search');
const taskInput = document.querySelector('.task-input');
const taskDescInput = document.querySelector('.task-desc-input');
const dueDate = document.querySelector('.due-date-input');
const taskButton = document.querySelector('.task-button');
const taskList = document.querySelector('.task-list');
const filterByStatus = document.querySelector('.filter-tasks');
const sortByPriority = document.querySelector('.sort-tasks');
const sortByDateBtn = document.querySelector('.sort-date-btn');

// Event Listeners
document.addEventListener('DOMContentLoaded', checkAuth);
loginForm?.addEventListener('submit', handleLogin);
registerForm?.addEventListener('submit', handleRegister);
showRegisterBtn?.addEventListener('click', () => toggleAuthForms('register'));
showLoginBtn?.addEventListener('click', () => toggleAuthForms('login'));
logoutBtn?.addEventListener('click', handleLogout);
taskButton?.addEventListener('click', addTask);
taskList?.addEventListener('click', handleTaskClick);
filterByStatus?.addEventListener('change', filterStatus);
sortByPriority?.addEventListener('change', sortPriority);
sortByDateBtn?.addEventListener('click', sortByDueDate);
search?.addEventListener('input', searchTasks);


function checkAuth() {
    const token = localStorage.getItem('access_token');
    if (token) {
        showTaskSection();
        getTasks();
    } else {
        showAuthSection();
    }
}

function showAuthSection() {
    if (authSection) authSection.style.display = 'block';
    if (taskSection) taskSection.style.display = 'none';
}

function showTaskSection() {
    if (authSection) authSection.style.display = 'none';
    if (taskSection) taskSection.style.display = 'block';
}

function toggleAuthForms(form) {
    if (form === 'register') {
        loginForm.style.display = 'none';
        registerForm.style.display = 'block';
    } else {
        registerForm.style.display = 'none';
        loginForm.style.display = 'block';
    }
}

async function handleLogin(e) {
    e.preventDefault();
    const username = document.querySelector('#login-username').value;
    const password = document.querySelector('#login-password').value;

    try {
        const response = await fetch(`${AUTH_URL}login/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password })
        });

        if (response.ok) {
            const data = await response.json();
            localStorage.setItem('access_token', data.access);
            localStorage.setItem('refresh_token', data.refresh);
            localStorage.setItem('username', data.username);
            showTaskSection();
            await getTasks();
        } else {
            alert('Login failed! Check your credentials.');
        }
    } catch (error) {
        console.error('Login error:', error);
        alert('Login failed! Check console for details.');
    }
}

async function handleRegister(e) {
    e.preventDefault();
    const username = document.querySelector('#register-username').value;
    const email = document.querySelector('#register-email').value;
    const password = document.querySelector('#register-password').value;

    try {
        const response = await fetch(`${AUTH_URL}register/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, email, password })
        });

        if (response.ok) {
            const data = await response.json();
            localStorage.setItem('access_token', data.access);
            localStorage.setItem('refresh_token', data.refresh);
            localStorage.setItem('username', data.user.username);
            showTaskSection();
            await getTasks();
        } else {
            const error = await response.json();
            alert(`Registration failed: ${JSON.stringify(error)}`);
        }
    } catch (error) {
        console.error('Registration error:', error);
        alert('Registration failed! Check console for details.');
    }
}

function handleLogout() {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    localStorage.removeItem('username');
    taskList.innerHTML = '';
    showAuthSection();
}


async function fetchData(url, method = "GET", data = null) {
    const token = localStorage.getItem('access_token');
    const options = {
        method,
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        }
    };
    if (data) options.body = JSON.stringify(data);

    const res = await fetch(url, options);
    

    if (res.status === 401) {
        const refreshed = await refreshAccessToken();
        if (refreshed) {
            options.headers['Authorization'] = `Bearer ${localStorage.getItem('access_token')}`;
            const retryRes = await fetch(url, options);
            return retryRes.ok ? retryRes.json() : null;
        } else {
            handleLogout();
            return null;
        }
    }
    
    return res.ok ? res.json() : null;
}

async function refreshAccessToken() {
    const refreshToken = localStorage.getItem('refresh_token');
    if (!refreshToken) return false;

    try {
        const response = await fetch(`${AUTH_URL}token/refresh/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ refresh: refreshToken })
        });

        if (response.ok) {
            const data = await response.json();
            localStorage.setItem('access_token', data.access);
            return true;
        }
    } catch (error) {
        console.error('Token refresh failed:', error);
    }
    return false;
}


async function getTasks() {
    taskList.innerHTML = '';
    const tasks = await fetchData(BASE_URL);
    if (!tasks) return;
    tasks.forEach(task => renderTask(task));
}

async function addTask(e) {
    e.preventDefault();
    if (!taskInput.value.trim()) return;

    const editId = taskButton.dataset.editId;

    if (editId) {
        const updated = await fetchData(`${BASE_URL}${editId}/`, "PATCH", {
            title: taskInput.value,
            description: taskDescInput.value,
            due_date: dueDate.value || null
        });

        if (updated) {
            await getTasks();
            taskButton.innerText = '➕';
            delete taskButton.dataset.editId;
        }
    } else {
        const newTask = {
            title: taskInput.value,
            description: taskDescInput.value,
            due_date: dueDate.value || null,
            priority: "low",
            status: "pending"
        };

        const created = await fetchData(BASE_URL, "POST", newTask);
        if (created) {
            renderTask(created);
        } else {
            alert('Failed to create task!');
        }
    }

    taskInput.value = '';
    taskDescInput.value = '';
    dueDate.value = '';
}

function renderTask(task) {
    const taskDiv = document.createElement('div');
    taskDiv.classList.add('task');
    if (task.status === 'completed') taskDiv.classList.add('completed');
    taskDiv.dataset.id = task.id;

    const contentDiv = document.createElement('div');
    contentDiv.classList.add('task-content');

    const leftDiv = document.createElement('div');
    
    const newTask = document.createElement('li');
    newTask.innerText = task.title;
    newTask.classList.add('task-item');
    leftDiv.appendChild(newTask);

    const newDate = document.createElement('div');
    newDate.innerText = task.due_date ? task.due_date.split("T")[0] : '';
    newDate.classList.add('due-date');
    leftDiv.appendChild(newDate);

    contentDiv.appendChild(leftDiv);

    // Buttons
    const buttonContainer = document.createElement('div');
    buttonContainer.classList.add('task-buttons');

    // Complete button
    const completedButton = document.createElement('button');
    completedButton.innerHTML = '<i class="fas fa-check"></i>';
    completedButton.classList.add('complete-btn');
    buttonContainer.appendChild(completedButton);

    // Priority button
    const priorityButton = document.createElement('button');
    priorityButton.classList.add('priority-status');
    let priorityMap = { 'low': 1, 'medium': 2, 'high': 3 };
    let reversePriorityMap = {1: 'low', 2: 'medium', 3: 'high'};
    let p = priorityMap[task.priority] || 1;
    priorityButton.dataset.priority = p;
    updatePriorityButtonText(priorityButton, p);
    priorityButton.addEventListener('click', async () => {
        let current = parseInt(priorityButton.dataset.priority);
        let next = (current % 3) + 1;
        priorityButton.dataset.priority = next;
        updatePriorityButtonText(priorityButton, next);

        await fetchData(`${BASE_URL}${task.id}/`, "PATCH", { priority: reversePriorityMap[next] });
    });
    buttonContainer.appendChild(priorityButton);

    // Delete button
    const deleteButton = document.createElement('button');
    deleteButton.innerHTML = '<i class="fas fa-trash"></i>';
    deleteButton.classList.add('trash-btn');
    buttonContainer.appendChild(deleteButton);

    // Edit button
    const editButton = document.createElement('button');
    editButton.innerHTML = '<i class="fas fa-edit"></i>';
    editButton.classList.add('edit-btn');
    buttonContainer.appendChild(editButton);

    contentDiv.appendChild(buttonContainer);
    taskDiv.appendChild(contentDiv);


    const newDesc = document.createElement('p');
    newDesc.innerText = task.description || '';
    newDesc.classList.add('task-desc');
    taskDiv.appendChild(newDesc);

    taskList.appendChild(taskDiv);

    taskDiv.addEventListener('click', (e) => {
        if (e.target.closest('button')) return;
        taskDiv.classList.toggle('show-desc');
    });
}

function updatePriorityButtonText(btn, value) {
    if (value === 1) btn.innerHTML = '🔵 Low';
    else if (value === 2) btn.innerHTML = '🟡 Medium';
    else btn.innerHTML = '🔴 High';
}

async function handleTaskClick(e) {
    e.preventDefault();
    const task = e.target.closest('.task');
    if (!task) return;
    const id = task.dataset.id;

    if (e.target.closest('.trash-btn')) {
        task.classList.add('fall');
        await fetchData(`${BASE_URL}${id}/`, "DELETE");
        task.addEventListener('transitionend', () => task.remove());
    }

    if (e.target.closest('.complete-btn')) {
        const isCompleted = task.classList.contains('completed');
        const newStatus = isCompleted ? 'pending' : 'completed';
        await fetchData(`${BASE_URL}${id}/`, "PATCH", { status: newStatus });
        task.classList.toggle('completed');
    }

    if (e.target.closest('.edit-btn')) {
        const title = task.querySelector('.task-item').innerText;
        const desc = task.querySelector('.task-desc').innerText;
        const date = task.querySelector('.due-date').innerText;

        taskInput.value = title;
        taskDescInput.value = desc;
        dueDate.value = date;

        taskButton.innerText = 'Update Task';
        taskButton.dataset.editId = id;
    }
}

function filterStatus(e) {
    const tasks = taskList.childNodes;
    tasks.forEach(task => {
        if (task.nodeType !== 1) return;
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
    const selectedPriority = e.target.value;
    const tasks = taskList.childNodes;
    
    tasks.forEach(task => {
        if (task.nodeType !== 1) return;
        
        const priorityBtn = task.querySelector('.priority-status');
        const taskPriority = parseInt(priorityBtn.dataset.priority);
        const priorityMap = { 'high': 3, 'medium': 2, 'low': 1 };
        
        if (selectedPriority === 'all' || taskPriority === priorityMap[selectedPriority]) {
            task.style.display = 'flex';
        } else {
            task.style.display = 'none';
        }
    });
}

function sortByDueDate() {
    const tasks = Array.from(taskList.children);
    tasks.sort((a, b) => {
        const dateA = new Date(a.querySelector('.due-date').innerText);
        const dateB = new Date(b.querySelector('.due-date').innerText);
        return dateA - dateB;
    });
    tasks.forEach(task => taskList.appendChild(task));
}

function searchTasks(e) {
    const searchTerm = e.target.value.toLowerCase();
    const tasks = taskList.childNodes;
    
    tasks.forEach(task => {
        if (task.nodeType !== 1) return;
        
        const title = task.querySelector('.task-item').innerText.toLowerCase();
        const description = task.querySelector('.task-desc')?.innerText.toLowerCase() || '';
        
        if (title.includes(searchTerm) || description.includes(searchTerm)) {
            task.style.display = 'flex';
        } else {
            task.style.display = 'none';
        }
    });
}