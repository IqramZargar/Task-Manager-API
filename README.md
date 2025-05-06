# 📝 Task Manager API

A simple backend project built with Django and Django REST Framework to manage personal tasks — including creating, updating, and deleting tasks through a RESTful API.

---

## ⚙️ Features

- ✅ Create new tasks  
- 📋 View task list  
- 🛠️ Update task details  
- ❌ Delete tasks  
- 📌 Mark tasks as completed  

---

## 🛠️ Tech Stack

- Python  
- Django  
- Django REST Framework  
- SQLite (default for development)  

---

## 📁 Project Structure

Task-Manager-API/
├── My_Proj/ # Django project settings
│ └── settings.py
│ └── urls.py
├── My_App/ # Main app for task logic
│ └── models.py
│ └── views.py
│ └── serializers.py
│ └── urls.py
├── db.sqlite3
├── manage.py
└── README.md

---

## 🔌 API Endpoints

All endpoints are under: `http://localhost:8000/api/`

| Method | Endpoint         | Description            |
|--------|------------------|------------------------|
| GET    | `/tasks/`        | Get all tasks          |
| POST   | `/tasks/`        | Create a new task      |
| GET    | `/tasks/<id>/`   | Get a task by ID       |
| PUT    | `/tasks/<id>/`   | Update a task by ID    |
| DELETE | `/tasks/<id>/`   | Delete a task by ID    |

---

## 🚀 Getting Started (Local Setup)

### 1. Clone the Repository

```bash
git clone https://github.com/IqramZargar/Task-Manager-API.git
cd Task-Manager-API

2. Create a Virtual Environment (optional but recommended)
bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Required Libraries
bash

pip install django
pip install djangorestframework
4. Run Migrations
bash

python manage.py migrate
5. Start the Development Server
bash

python manage.py runserver
Then open in browser or Postman:

bash

http://localhost:8000/api/tasks/
📦 Example JSON for Creating a Task (POST)
json

{
  "title": "Buy groceries",
  "description": "Milk, Bread, Eggs",
  "due_date": "2025-05-10",
  "is_completed": false
}
📄 License
This project is open-source and free to use.

🤝 Contributing
Contributions are welcome! Feel free to fork the project and submit a pull request.
