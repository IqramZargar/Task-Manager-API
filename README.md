# 📝 Task Manager API

A simple RESTful API built with Django and Django REST Framework for managing tasks — add, update, delete, and track completion status of daily tasks.

---

## ⚙️ Features

- ✅ Create new tasks  
- 📋 List all tasks  
- 🛠️ Update task details  
- ❌ Delete tasks  
- ⏰ Add due dates  
- 📌 Mark tasks as completed  

---

## 🛠️ Tech Stack

- Python  
- Django  
- Django REST Framework  
- SQLite (for easy local dev)  

---

## 📁 Project Structure

taskmanager_project/
├── My_Proj/ # Main project settings
│ ├── settings.py
│ ├── urls.py
│ └── ...
├── My_App/ # Django app for task logic
│ ├── models.py
│ ├── views.py
│ ├── serializers.py
│ └── urls.py
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md

yaml
---

## 🔌 API Endpoints

Base URL: `http://localhost:8000/api/`

| Method | Endpoint        | Description             |
|--------|------------------|-------------------------|
| GET    | `/tasks/`        | List all tasks          |
| POST   | `/tasks/`        | Create a new task       |
| GET    | `/tasks/<id>/`   | Retrieve task details   |
| PUT    | `/tasks/<id>/`   | Update a task           |
| DELETE | `/tasks/<id>/`   | Delete a task           |

---

## 🚀 Getting Started

### 🔧 Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/IqramZargar/Task-Manager-API
   cd Task-Manager-API
(Optional but recommended) Create a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash

pip install -r requirements.txt
Run migrations:

bash
Copy
Edit
python manage.py migrate
Start the server:

bash

python manage.py runserver
Open in browser or test using Postman:

bash

http://localhost:8000/api/tasks/
📦 Example JSON (POST Body)

json


{
  "title": "Complete assignment",
  "description": "Finish writing README for task manager",
  "due_date": "2025-05-06",
  "is_completed": false
}


📄 License
This project is open-source and free to use.

🤝 Contributing
Pull requests are welcome. For major changes, open an issue first to discuss what you'd like to change.
