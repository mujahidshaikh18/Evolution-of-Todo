from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlmodel import Session, select
from datetime import datetime

# Import with absolute paths to avoid relative import issues
from db import engine
from models import Task
from schemas import TaskCreate, TaskUpdate, TaskResponse, MessageResponse, TaskToggleComplete
from middleware.auth import validate_user_access

router = APIRouter()

@router.get("/tasks", response_model=List[TaskResponse])
def get_tasks(user_id: str = Depends(validate_user_access)):
    """Get all tasks for the authenticated user"""
    with Session(engine) as session:
        statement = select(Task).where(Task.user_id == user_id)
        tasks = session.exec(statement).all()
        return tasks

@router.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task_create: TaskCreate, user_id: str = Depends(validate_user_access)):
    """Create a new task for the authenticated user"""
    with Session(engine) as session:
        task = Task(
            title=task_create.title,
            description=task_create.description,
            completed=False,
            user_id=user_id
        )
        session.add(task)
        session.commit()
        session.refresh(task)
        return task

@router.get("/tasks/{id}", response_model=TaskResponse)
def get_task(id: int, user_id: str = Depends(validate_user_access)):
    """Get a specific task by ID"""
    with Session(engine) as session:
        statement = select(Task).where(Task.id == id, Task.user_id == user_id)
        task = session.exec(statement).first()
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return task

@router.put("/tasks/{id}", response_model=TaskResponse)
def update_task(id: int, task_update: TaskUpdate, user_id: str = Depends(validate_user_access)):
    """Update a specific task by ID"""
    with Session(engine) as session:
        statement = select(Task).where(Task.id == id, Task.user_id == user_id)
        task = session.exec(statement).first()

        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

        # Update task fields if provided
        if task_update.title is not None:
            task.title = task_update.title
        if task_update.description is not None:
            task.description = task_update.description

        task.updated_at = datetime.utcnow()
        session.add(task)
        session.commit()
        session.refresh(task)
        return task

@router.delete("/tasks/{id}", response_model=MessageResponse)
def delete_task(id: int, user_id: str = Depends(validate_user_access)):
    """Delete a specific task by ID"""
    with Session(engine) as session:
        statement = select(Task).where(Task.id == id, Task.user_id == user_id)
        task = session.exec(statement).first()

        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

        session.delete(task)
        session.commit()
        return {"message": "Task deleted"}

@router.patch("/tasks/{id}/complete", response_model=TaskResponse)
def toggle_task_completion(id: int, toggle: TaskToggleComplete, user_id: str = Depends(validate_user_access)):
    """Toggle task completion status"""
    with Session(engine) as session:
        statement = select(Task).where(Task.id == id, Task.user_id == user_id)
        task = session.exec(statement).first()

        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

        task.completed = toggle.completed
        task.updated_at = datetime.utcnow()
        session.add(task)
        session.commit()
        session.refresh(task)
        return task