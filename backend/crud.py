from sqlalchemy.orm import Session
import models
import schemas


# Register User
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        name=user.name,
        email=user.email,
        password=user.password
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


# Login User
def login_user(db: Session, email: str, password: str):
    return db.query(models.User).filter(
        models.User.email == email,
        models.User.password == password
    ).first()

def create_task(db: Session, task: schemas.TaskCreate):
    new_task = models.Task(
        title=task.title,
        description=task.description,
        status=task.status,
        user_id=task.user_id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task 

def get_tasks(db: Session):
    return db.query(models.Task).all()

def update_task(db: Session, task_id: int, title: str, description: str, status: str):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if task:
        task.title = title
        task.description = description
        task.status = status

        db.commit()
        db.refresh(task)

    return task

def delete_task(db: Session, task_id: int):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if task:
        db.delete(task)
        db.commit()

    return task