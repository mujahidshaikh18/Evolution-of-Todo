from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class User(SQLModel, table=True):
    id: str = Field(primary_key=True) # UUID string
    email: str = Field(index=True, unique=True)
    name: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

class TaskBase(SQLModel):
    title: str = Field(min_length=1, max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: bool = Field(default=False)
    user_id: str  # Changed from foreign_key="users.id" since we're not implementing a separate users table

class Task(TaskBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str = Field(foreign_key="user.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class TaskCreate(TaskBase):
    pass

class TaskUpdate(SQLModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)

class TaskPublic(TaskBase):
    id: int
    user_id: str
    created_at: datetime
    updated_at: datetime