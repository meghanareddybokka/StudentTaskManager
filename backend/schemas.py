from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
class UserLogin(BaseModel):
    email: EmailStr
    password: str  
class TaskCreate(BaseModel):
    title: str
    description: str
    status: str
    user_id: int

class TaskUpdate(BaseModel):
    title: str
    description: str
    status: str
              