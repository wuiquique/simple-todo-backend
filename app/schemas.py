from pydantic import BaseModel

class UserLogin(BaseModel):
    username: str

class UserCreate(BaseModel):
    name: str
    username: str

class ProjectCreate(BaseModel):
    name: str
    userId: int

class TaskCreate(BaseModel):
    title: str
    isCompleted: bool
    due: str
    projectId: int

class ToggleTask(BaseModel):
    isCompleted: bool
