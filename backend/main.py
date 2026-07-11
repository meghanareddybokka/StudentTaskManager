from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import models
import crud
import schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Welcome to Student Task Manager API"}


@app.post("/register")
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = crud.create_user(db, user)

    return {
        "message": "User registered successfully",
        "user_id": new_user.id
    }
@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.login_user(db, user.email, user.password)

    if not db_user:
        return {
            "message": "Invalid email or password"
        }

    return {
        "message": "Login successful",
        "user_id": db_user.id,
        "name": db_user.name
    }
@app.post("/tasks")
def add_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    new_task = crud.create_task(db, task)

    return {
        "message": "Task created successfully",
        "task_id": new_task.id
    }

@app.get("/tasks")
def get_all_tasks(db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db)
    return tasks

@app.put("/tasks/{task_id}")
def update_task(
    task_id: int,
    task: schemas.TaskUpdate,
    db: Session = Depends(get_db)
):
    updated_task = crud.update_task(
        db,
        task_id,
        task.title,
        task.description,
        task.status
    )

    if not updated_task:
        return {"message": "Task not found"}

    return {
        "message": "Task updated successfully"
    }

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    deleted_task = crud.delete_task(db, task_id)

    if not deleted_task:
        return {"message": "Task not found"}

    return {
        "message": "Task deleted successfully"
    }