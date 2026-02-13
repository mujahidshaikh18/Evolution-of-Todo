from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from datetime import datetime

# Import with absolute paths to avoid relative import issues
from db import get_session
from models import Task
from schemas import TaskCreate, TaskUpdate, TaskResponse, MessageResponse, TaskToggleComplete
from middleware.auth import validate_user_access

router = APIRouter()

@router.get("/tasks", response_model=List[TaskResponse])
async def get_tasks(user_id: str = Depends(validate_user_access), session: AsyncSession = Depends(get_session)):
    """Get all tasks for the authenticated user"""
    statement = select(Task).where(Task.user_id == user_id)
    result = await session.exec(statement)
    tasks = result.all()
    return tasks

@router.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(task_create: TaskCreate, user_id: str = Depends(validate_user_access), session: AsyncSession = Depends(get_session)):
    """Create a new task for the authenticated user"""
    task = Task(
        title=task_create.title,
        description=task_create.description,
        completed=False,
        user_id=user_id
    )
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return task

@router.get("/tasks/{id}", response_model=TaskResponse)
async def get_task(id: int, user_id: str = Depends(validate_user_access), session: AsyncSession = Depends(get_session)):
    """Get a specific task by ID"""
    statement = select(Task).where(Task.id == id, Task.user_id == user_id)
    result = await session.exec(statement)
    task = result.first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/tasks/{id}", response_model=TaskResponse)
async def update_task(id: int, task_update: TaskUpdate, user_id: str = Depends(validate_user_access), session: AsyncSession = Depends(get_session)):
    """Update a specific task by ID"""
    statement = select(Task).where(Task.id == id, Task.user_id == user_id)
    result = await session.exec(statement)
    task = result.first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Update task fields if provided
    if task_update.title is not None:
        task.title = task_update.title
    if task_update.description is not None:
        task.description = task_update.description

    task.updated_at = datetime.utcnow()
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return task

@router.delete("/tasks/{id}", response_model=MessageResponse)
async def delete_task(id: int, user_id: str = Depends(validate_user_access), session: AsyncSession = Depends(get_session)):
    """Delete a specific task by ID"""
    statement = select(Task).where(Task.id == id, Task.user_id == user_id)
    result = await session.exec(statement)
    task = result.first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    await session.delete(task)
    await session.commit()
    return {"message": "Task deleted"}

@router.patch("/tasks/{id}/complete", response_model=TaskResponse)
async def toggle_task_completion(id: int, toggle: TaskToggleComplete, user_id: str = Depends(validate_user_access), session: AsyncSession = Depends(get_session)):
    """Toggle task completion status"""
    statement = select(Task).where(Task.id == id, Task.user_id == user_id)
    result = await session.exec(statement)
    task = result.first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.completed = toggle.completed
    task.updated_at = datetime.utcnow()
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return task