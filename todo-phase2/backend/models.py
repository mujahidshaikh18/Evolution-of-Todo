from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
import uuid

class User(SQLModel, table=True):
    __tablename__ = "user"
    __table_args__ = {'extend_existing': True}
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
    __tablename__ = "task"
    __table_args__ = {'extend_existing': True}
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


class ChatHistory(SQLModel, table=True):
    __tablename__ = "chathistory"
    __table_args__ = {'extend_existing': True}
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    session_id: str = Field(index=True)
    role: str = Field(max_length=20)  # "user", "assistant", "system"
    content: str = Field(max_length=10000)
    created_at: datetime = Field(default_factory=datetime.utcnow)