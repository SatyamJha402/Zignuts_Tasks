-------------------📝 Django Blog App-------------------  
A fully functional blog web application built with Django.  
Users can sign up, log in, create, edit, and delete their posts — all with profile management and image uploads.  

-------------------🚀 Features-------------------  
-User authentication (Register, Login, Logout)  
-Create, update, and delete blog posts  
-Profile management with profile pictures  
-Automatic profile creation using Django signals  
-Clean and responsive UI with Bootstrap 4 and Crispy Forms

-------------------🧱 Apps Overview-------------------  
---blog/  
-Handles all blog-related functionality:  
-List, detail, create, update, and delete posts  
-Post ownership linked to authenticated users  
-Templates extend a shared base.html layout  

---users/  
-Handles user management:  
  User registration and login system  
-Profile page with update form for username, email, and image  
-Image resizing handled in models.py using Pillow  
-Auto-profile creation and saving via signals.py  

-------------------⚙️ Tech Stack-------------------  
-Backend: Django  
-Frontend: HTML, CSS, Bootstrap 4  
-Database: SQLite (default)  
-Libraries: Pillow, Django Crispy Forms  
