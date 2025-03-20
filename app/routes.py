from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from . import controllers, database, schemas

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def is_running():
    return True

@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    return controllers.login(db=db, user=user)

@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return controllers.create_user(db=db, user=user)

@router.delete("/user/{userId}")
def delete_user(userId: int, db: Session = Depends(get_db)):
    return controllers.delete_user(db=db, userId=userId)

@router.get("/projects/{userId}")
def get_projects(userId: int, db: Session = Depends(get_db)):
    return controllers.get_projects(db=db, userId=userId)

@router.post("/projects")
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    return controllers.create_project(db=db, project=project)

@router.delete("/projects/{projectId}")
def delete_project(projectId: int, db: Session = Depends(get_db)):
    return controllers.delete_project(db=db, projectId=projectId)

@router.get("/tasks/{projectId}")
def get_tasks(projectId: int, db: Session = Depends(get_db)):
    return controllers.get_tasks(db=db, projectId=projectId)

@router.post("/tasks")
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return controllers.create_task(db=db, task=task)

@router.patch("/tasks/{taskId}")
def toogle_task(taskId: int, db: Session = Depends(get_db)):
    return controllers.toogle_task(db=db, taskId=taskId)

@router.patch("/tasks/{projectId}/toggle")
def toggle_all_tasks(projectId: int, toggle: schemas.ToggleTask, db: Session = Depends(get_db)):
    return controllers.toogle_all_tasks(db=db, projectId=projectId, isCompleted=toggle.isCompleted)

@router.delete("/tasks/{taskId}")
def delete_task(taskId: int, db: Session = Depends(get_db)):
    return controllers.delete_task(db=db, taskId=taskId)
