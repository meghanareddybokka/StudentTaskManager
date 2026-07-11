# Student Task Manager

## Project Overview

Student Task Manager is a web-based application developed to help students organize and manage their daily academic tasks efficiently. It allows users to register, log in securely, and manage their tasks through a simple and user-friendly interface.

## Features

- User Registration
- User Login
- Add New Tasks
- View All Tasks
- Delete Tasks
- FastAPI REST APIs
- MySQL Database Integration

## Technologies Used

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- FastAPI

### Database
- MySQL
- SQLAlchemy

## Project Structure

```
StudentTaskManager/
│
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py
│   └── requirements.txt
│
├── frontend/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── css/
│   └── js/
│
└── README.md
```

## How to Run the Project

### Backend

1. Navigate to the backend folder.

```
cd backend
```

2. Activate the virtual environment.

3. Start the FastAPI server.

```
uvicorn main:app --reload
```

The backend runs at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

### Frontend

Open the frontend using Live Server.

```
login.html
```

## Workflow

1. Register a new account.
2. Login using your credentials.
3. Add new tasks.
4. View all tasks.
5. Delete completed tasks.

## Future Enhancements

- Update/Edit Tasks
- Task Priority
- Due Dates
- Search Tasks
- Responsive Mobile Design

## Author

**Meghana Reddy**

B.Tech Computer Science and Engineering

ACE Engineering College
