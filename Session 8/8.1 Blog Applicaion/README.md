# 📝 Django Blog Application

A **Blog Web Application** built using **Django**, developed as part of the **Minor Project**.  
It allows users to register, log in, create, edit, view, and delete blog posts, with integrated profile management and Django Admin for backend control.

---

## 📋 Assignment Requirements

### ✅ Feature Scope
- **User Authentication:** Login, Logout, and Signup using Django’s built-in authentication  
- **Blog Management:** Create, Edit, Delete blog posts  
- **View Posts:** List all posts and view individual post details  
- **Admin Management:** Use Django Admin to manage users and posts  
- **Styling:** Bootstrap for responsive and clean UI (optional)  

---

## 🚀 Features

- User authentication (Signup, Login, Logout)  
- CRUD functionality for blog posts  
- User profile creation and editing with image upload  
- Automatic profile creation using Django signals  
- Admin panel for managing users and blog posts  
- Responsive interface with **Bootstrap** and **Crispy Forms**

---

## Apps

### blog/  
- Handles all blog-related operations  
- Allows listing all posts, viewing post details, and creating/editing/deleting posts  
- Ensures post ownership is tied to authenticated users  
- Templates extend a shared `base.html` layout for consistency  

### users/  
- Manages user registration, login, and logout  
- Handles user profile management (username, email, and profile image)  
- Uses Django signals to automatically create and update user profiles

---
  
## 🧩 Tech Stack

- **Backend:** Django  
- **Frontend:** HTML, CSS, Bootstrap  
- **Database:** SQLite (default)  
- **Libraries:** Pillow, Django Crispy Forms  

---

## 📁 Project Structure  
project_root/  
│  
├── db.sqlite3  
├── manage.py  
│  
├── blog/  
│ ├── admin.py  
│ ├── apps.py  
│ ├── models.py  
│ ├── tests.py  
│ ├── urls.py  
│ ├── views.py  
│ │  
│ ├── migrations
│ │  
│ ├── static/  
│ │ └── blog/  
│ │ └── main.css  
│ │  
│ └── templates/  
│ └── blog/  
│ ├── about.html  
│ ├── base.html  
│ ├── home.html  
│ ├── post_confirm_delete.html  
│ ├── post_detail.html  
│ └── post_form.html  
│  
├── django_project/  
│ ├── asgi.py  
│ ├── settings.py  
│ ├── urls.py  
│ ├── wsgi.py  
│ └── init.py  
│  
├── media/  
│ ├── default.jpg  
│ └── profile_pics/  
│ ├── default.png  
│ ├── Screenshot_2025-03-01_224542.jpg  
│ ├── Screenshot_2025-03-05_170320.png  
│ └── Screenshot_2025-03-05_170320_wTk8vgY.png  
│  
└── users/  
├── admin.py  
├── apps.py  
├── forms.py  
├── models.py  
├── signals.py  
├── tests.py  
├── views.py  
│  
├── migrations/  
│ └── 0001_initial.py  
│  
└── templates/  
└── users/  
├── login.html  
├── logout.html  
├── profile.html  
└── register.html  
