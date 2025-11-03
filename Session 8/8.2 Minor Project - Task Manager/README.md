# 🧩 Task Manager API

A fully functional **RESTful API** built using **Django REST Framework (DRF)** and **JWT Authentication**.  
This backend powers a task management system where users can register, authenticate, and perform CRUD operations on their tasks.

---

## 🚀 Features

### 🔐 Authentication
- JWT-based authentication (`access` and `refresh` tokens)
- Secure endpoints with token protection
- Token refresh mechanism for session continuation

### ✅ Task Management API
- Create, retrieve, update, and delete tasks
- Track **completion status**, **priority levels**, and **due dates**
- Automatically link tasks to their respective users

### ⚙️ Developer-Friendly
- RESTful design
- Clear endpoint structure
- Easily integrable with any frontend (React, Vue, or Vanilla JS)

---

## 🧠 Tech Stack

| Layer | Technology |
|-------|-------------|
| **Backend** | Django, Django REST Framework |
| **Database** | PostgreSQL |
| **Authentication** | JSON Web Token (JWT) |

---

## 🗂️ Folder Structure

task_manager/  
│ manage.py  
│ taskpro_db  
│  
├───tasks  
│ │ admin.py  
│ │ apps.py  
│ │ models.py  
│ │ serializers.py  
│ │ tests.py  
│ │ urls.py  
│ │ views.py  
│ │ init.py  
│ │  
│ ├───migrations/  
│ └───pycache  
│  
└───task_manager  
│ | asgi.py  
│ | settings.py  
│ | urls.py  
│ | wsgi.py  
│ | init.py  
│  
└───pycache  
