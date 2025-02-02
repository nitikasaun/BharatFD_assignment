# FAQ Management System (Django Backend)

## 📌 Project Overview

This is a **Django-based FAQ Management System** with multilingual support. It allows users to store FAQs, translate them into multiple languages, and retrieve data via a **REST API** with caching enabled using Redis.

---

## 🚀 Installation Guide

### **1. Prerequisites**

Ensure you have the following installed:

- Python 3.8+
- Django 4+
- Redis
- Virtual environment (recommended)

### **2. Clone the Repository**
```sh
git clone https://github.com/yourusername/faq-management.git
cd faq-management
```

### **3. Set Up Virtual Environment**
```sh
python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### **4. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **5. Configure Database & Migrations**
```sh
python manage.py migrate
python manage.py createsuperuser  # Create an admin user
```

### **6. Start Redis Server**
Make sure Redis is running:
```sh
redis-server
```

### **7. Run the Development Server**
```sh
python manage.py runserver
```

Access the project at **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**
---

## 🛠️ Running the Application in VS Code
### **1. Open the Project in VS Code**
```sh
cd path/to/faq-management
code .
```

### **2. Activate the Virtual Environment**
```sh
# On macOS/Linux:
source venv/bin/activate  
# On Windows:
venv\Scripts\activate
```

### **3. Start Redis Server**
Ensure Redis is running before starting the Django application:
```sh
redis-server
```

### **4. Run the Django Development Server**
```sh
python manage.py runserver
```

Visit **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** in your browser.

### **5. Test API Endpoints Using REST Client in VS Code**
1. Install the **REST Client** extension in VS Code.
2. Create a new file `test.http` and add:
   ```http
   GET http://127.0.0.1:8000/api/faqs/?lang=en
   ```
3. Click **Send Request** to test the API.

Alternatively, you can use **Thunder Client** or **Postman** for API testing.

---

## 📌 API Endpoints
### **1. Get All FAQs**
**GET /api/faqs/**
```sh
curl -X GET "http://127.0.0.1:8000/api/faqs/?lang=hi"
```

**Response:**
```json
[
  {
    "id": 1,
    "translated_question": "डिजैंगो क्या है?",
    "answer": "Django is a high-level Python Web framework."
  }
]
```

### **2. Create a New FAQ**
**POST /api/faqs/**
```sh
curl -X POST "http://127.0.0.1:8000/api/faqs/" \
     -H "Content-Type: application/json" \
     -d '{"question": "What is Django?", "answer": "Django is a Python framework", "language": "en"}'
```

### **3. Get a Specific FAQ by ID**
**GET /api/faqs/{id}**
```sh
curl -X GET "http://127.0.0.1:8000/api/faqs/1/"
```

### **4. Delete an FAQ**
**DELETE /api/faqs/{id}**
```sh
curl -X DELETE "http://127.0.0.1:8000/api/faqs/1/"
```

## 👥 Contribution Guidelines
We welcome contributions! Follow these steps to contribute:

### **1. Fork the Repository**
Click the **Fork** button on GitHub to create your own copy.

### **2. Clone Your Forked Repository**
```sh
git clone https://github.com/yourusername/faq-management.git
cd faq-management
```

### **3. Create a New Branch**
```sh
git checkout -b feature-new-update
```

### **4. Make Changes & Commit**
Follow **conventional commit messages**:
```sh
git commit -m "feat: Add support for new language translations"
```

### **5. Push Changes & Create Pull Request**
```sh
git push origin feature-new-update
```

Submit a **Pull Request (PR)** on GitHub.

---



## 📄 Requirements File
Create a `requirements.txt` file with the following dependencies:
```txt
Django>=4.0
django-ckeditor
redis
django-redis
googletrans==4.0.0-rc1
djangorestframework
dotenv
pytest
flake8
```
To install the dependencies, run:
```sh
pip install -r requirements.txt