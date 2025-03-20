from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import HTTPException
from . import models, schemas

def login(db: Session, user: schemas.UserLogin):
    user_db = db.query(models.User).filter(models.User.username == user.username).first()
    if not user_db:
        raise HTTPException(status_code=400, detail="Usuario no encontrado o credenciales inválidas")
    return user_db

def create_user(db: Session, user: schemas.UserCreate):
    existing_user = db.query(models.User).filter(models.User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    db_user = models.User(**user.model_dump())
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al crear usuario: {str(e)}")
    return db_user

def delete_user(db: Session, userId: int):
    user = db.query(models.User).filter(models.User.id == userId).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    try:
        db.delete(user)
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al eliminar usuario: {str(e)}")
    return {"message": "Usuario eliminado exitosamente"}

def get_projects(db: Session, userId: int):
    projects = db.query(
        models.Project,
        func.count(models.Task.id).label("task_total"),
        func.count(models.Task.id).filter(models.Task.isCompleted == True).label("task_completed")
    ).outerjoin(models.Task, models.Project.id == models.Task.projectId) \
     .filter(models.Project.userId == userId) \
     .group_by(models.Project.id).all()

    if not projects:
        return []

    result = [
        {
            "id": project.id,
            "name": project.name,
            "userId": project.userId,
            "task_total": task_total,
            "task_completed": task_completed
        }
        for project, task_total, task_completed in projects
    ]

    return result

def create_project(db: Session, project: schemas.ProjectCreate):
    db_project = models.Project(**project.model_dump())
    try:
        db.add(db_project)
        db.commit()
        db.refresh(db_project)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al crear proyecto: {str(e)}")

    result = {
        "id": db_project.id,
        "name": db_project.name,
        "userId": db_project.userId,
        "task_total": 0,
        "task_completed": 0
    }
    return result

def delete_project(db: Session, projectId: int):
    project = db.query(models.Project).filter(models.Project.id == projectId).first()
    if not project:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")

    try:
        db.delete(project)
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al eliminar proyecto: {str(e)}")

    return {"message": "Proyecto eliminado exitosamente"}

def get_tasks(db: Session, projectId: int):
    tasks = db.query(models.Task).filter(models.Task.projectId == projectId).all()
    if not tasks:
        raise HTTPException(status_code=404, detail="No se encontraron tareas para este proyecto")
    return tasks

def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(**task.model_dump())
    try:
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al crear tarea: {str(e)}")
    return db_task

def delete_task(db: Session, taskId: int):
    task = db.query(models.Task).filter(models.Task.id == taskId).first()
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    try:
        db.delete(task)
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al eliminar tarea: {str(e)}")

    return {"message": "Tarea eliminada exitosamente"}
