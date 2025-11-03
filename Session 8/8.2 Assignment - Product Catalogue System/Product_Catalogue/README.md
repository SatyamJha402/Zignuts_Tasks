# 🛍️ Product Catalogue REST API

This project implements a **RESTful API for a Product Catalogue System** using **Django REST Framework (DRF)**.  
It supports complete CRUD operations (Create, Read, Update, Delete) for products, along with proper model validation and structured unit testing for reliability.

---

## 📋 Assignment Requirements

### ✅ Core Requirements
- **Endpoints:** GET, POST, PUT, DELETE for products  
- **Fields:**  
  - name  
  - description  
  - price
  - stock_quantity
  - category
- **Uses:**  
  - ModelViewSet and Router for clean routing  
  - ModelSerializer for validation and data serialization  
  - Validation logic (e.g., price must be > 0)

### 🧪 Testing Requirements
Comprehensive unit tests have been written for:
- **Model Tests:** Ensure Product model fields and string representation work correctly  
- **URL Tests:** Validate URL resolution and routing names  
- **View Tests:** Verify CRUD operations including:
  - Creating a product  
  - Fetching product list and details  
  - Updating and deleting a product  
  - Handling invalid scenarios (e.g., negative price)

---

## 🚀 Features
- RESTful API endpoints for product management  
- Validation on product creation and updates  
- Modular Django app structure  
- Separate test cases for models, URLs, and views  
- Uses DRF’s ModelViewSet, Router, and APIClient  
- JSON responses with proper status codes  

---

## 🧩 Tech Stack
- **Backend:** Django, Django REST Framework  
- **Database:** SQLite (default)  
- **Testing:** Django TestCase, APITestCase, APIClient  
- **Routing:** DRF Routers  
- **Serialization:** ModelSerializer  

---

## 📁 Project Structure
project_root/  
│  
├── Product_Catalogue/  
│ ├── __init__.py  
│ ├── asgi.py  
│ ├── settings.py  
│ ├── urls.py  
│ ├── wsgi.py  
│  
├── products/  
│ ├── models.py  
│ ├── serializers.py  
│ ├── views.py  
│ ├── urls.py  
│ ├── tests/  
│ ├──── test_models.py  
│ ├──── test_urls.py  
│ ├──── test_views.py  
│  
│── db.sqlite3  
└── manage.py  
