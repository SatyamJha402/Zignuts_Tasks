# 📝 Task Management App

A full-stack **Task Management System** built with **Django REST Framework (DRF)** for the backend and **Vanilla JavaScript** for the frontend.  
Users can register, log in via **JWT authentication**, and manage their tasks with features like priorities, due dates, sorting, filtering, and editing — all in a clean, interactive UI.

---

## 🚀 Features

### 🔐 Authentication
- User registration and login using **JWT** (access & refresh tokens)
- Secure API endpoints protected by token-based authentication
- Seamless token refresh for session continuity

### ✅ Task Management
- Add, edit, delete, and complete tasks  
- Set **priority levels** (`Low`, `Medium`, `High`)  
- Assign **due dates** for better tracking  
- Expand/collapse task descriptions  
- Visual priority highlighting  
- Instant updates with smooth UI transitions  

### 🔎 Additional Functionality
- Search tasks by title  
- Filter by completion status  
- Sort by due date or priority  
- Clean animations for better UX  

---

## 🧩 Tech Stack

| Layer | Technology |
|-------|-------------|
| **Backend** | Django, Django REST Framework |
| **Frontend** | Vanilla JavaScript, HTML5, CSS3 |
| **Database** | PostgreSQL |
| **Authentication** | JSON Web Tokens (JWT) |
| **Other Tools** | Crispy Forms (for backend UI), Axios / Fetch API |

---

## Folder Structure

├───frontend  
│   │   app.js  
│   │   index.html  
│   │   style.css  
│   │  
│   └───.vscode  
│           settings.json  
│  
└───task_manager  
    │   manage.py  
    │   taskpro_db  
    │  
    ├───tasks  
    │   │   admin.py  
    │   │   apps.py  
    │   │   models.py  
    │   │   serializers.py  
    │   │   tests.py  
    │   │   urls.py  
    │   │   views.py  
    │   │   __init__.py  
    │   │  
    │   ├───migrations/  
    │   │  
    │   └───__pycache__/  
    └───task_manager  
        │   asgi.py  
        │   settings.py  
        │   urls.py  
        │   wsgi.py  
        │   __init__.py  
        │  
        └───__pycache__/  
