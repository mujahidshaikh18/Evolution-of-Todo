"""
MCP Tool for managing todo items via CRUD operations
"""
import sys
from pathlib import Path
from typing import Dict, Any, Optional
from datetime import datetime
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

# Add the backend path to sys.path to import models and db
backend_path = Path(__file__).parent.parent.parent / "todo-phase2" / "backend"
if str(backend_path) not in sys.path:
    sys.path.insert(0, str(backend_path))

# Now import from backend
from models import Task, TaskCreate, TaskUpdate, User
from db import get_engine


class TodoMCPTask:
    def __init__(self):
        self.engine = get_engine()

    async def execute(self, operation: str, task_data: Optional[Dict[str, Any]] = None, task_id: Optional[str] = None, user_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Execute todo management operations

        Args:
            operation: Type of operation (create, read, update, delete, complete)
            task_data: Task details for create/update operations
            task_id: ID of task for read/update/delete operations
            user_id: ID of user for proper isolation

        Returns:
            Dictionary with operation result and affected task data
        """
        # Use async session since we need to properly await database operations
        async with AsyncSession(self.engine) as session:
            try:
                if operation == "create":
                    return await self._create_task(session, task_data, user_id)
                elif operation == "read":
                    return await self._read_task(session, int(task_id), user_id)
                elif operation == "update":
                    return await self._update_task(session, int(task_id), task_data, user_id)
                elif operation == "delete":
                    return await self._delete_task(session, int(task_id), user_id)
                elif operation == "complete":
                    return await self._toggle_complete(session, int(task_id), user_id)
                elif operation == "list":
                    return await self._list_tasks(session, user_id)
                else:
                    raise ValueError(f"Unsupported operation: {operation}")
            except Exception as e:
                return {
                    "success": False,
                    "error": str(e),
                    "operation": operation
                }

    async def _create_task(self, session: AsyncSession, task_data: Dict[str, Any], user_id: str) -> Dict[str, Any]:
        """Create a new task"""
        if not task_data or not user_id:
            raise ValueError("task_data and user_id are required for create operation")

        # Create task object from provided data
        task_dict = {**task_data, "user_id": user_id}
        task = Task(**task_dict)

        # Add to session and commit asynchronously
        session.add(task)
        await session.commit()
        await session.refresh(task)

        # Convert task to a dictionary that is JSON serializable
        task_dict = task.dict() if hasattr(task, 'dict') else {k: v for k, v in task.__dict__.items() if not k.startswith('_')}
        return {
            "success": True,
            "operation": "create",
            "task": task_dict
        }

    async def _read_task(self, session: AsyncSession, task_id: int, user_id: str) -> Dict[str, Any]:
        """Read a specific task"""
        statement = select(Task).where(Task.id == task_id).where(Task.user_id == user_id)
        result = await session.exec(statement)
        task = result.first()

        if not task:
            raise ValueError(f"Task with ID {task_id} not found for user {user_id}")

        # Convert task to a dictionary that is JSON serializable
        task_dict = task.dict() if hasattr(task, 'dict') else {k: v for k, v in task.__dict__.items() if not k.startswith('_')}
        return {
            "success": True,
            "operation": "read",
            "task": task_dict
        }

    async def _update_task(self, session: AsyncSession, task_id: int, task_data: Dict[str, Any], user_id: str) -> Dict[str, Any]:
        """Update an existing task"""
        statement = select(Task).where(Task.id == task_id).where(Task.user_id == user_id)
        result = await session.exec(statement)
        task = result.first()

        if not task:
            raise ValueError(f"Task with ID {task_id} not found for user {user_id}")

        # Update task with provided data
        for key, value in task_data.items():
            if hasattr(task, key):
                setattr(task, key, value)

        task.updated_at = datetime.utcnow()  # Update timestamp
        session.add(task)
        await session.commit()
        await session.refresh(task)

        # Convert task to a dictionary that is JSON serializable
        task_dict = task.dict() if hasattr(task, 'dict') else {k: v for k, v in task.__dict__.items() if not k.startswith('_')}
        return {
            "success": True,
            "operation": "update",
            "task": task_dict
        }

    async def _delete_task(self, session: AsyncSession, task_id: int, user_id: str) -> Dict[str, Any]:
        """Delete a task"""
        statement = select(Task).where(Task.id == task_id).where(Task.user_id == user_id)
        result = await session.exec(statement)
        task = result.first()

        if not task:
            raise ValueError(f"Task with ID {task_id} not found for user {user_id}")

        await session.delete(task)
        await session.commit()

        return {
            "success": True,
            "operation": "delete",
            "task_id": task_id
        }

    async def _toggle_complete(self, session: AsyncSession, task_id: int, user_id: str) -> Dict[str, Any]:
        """Toggle task completion status - Actually toggles the boolean state, not just sets to True"""
        statement = select(Task).where(Task.id == task_id).where(Task.user_id == user_id)
        result = await session.exec(statement)
        task = result.first()

        if not task:
            raise ValueError(f"Task with ID {task_id} not found for user {user_id}")

        # Toggle the completion state (True becomes False, False becomes True)
        task.completed = not task.completed
        task.updated_at = datetime.utcnow()  # Update timestamp
        await session.commit()
        await session.refresh(task)

        # Convert task to a dictionary that is JSON serializable
        task_dict = task.dict() if hasattr(task, 'dict') else {k: v for k, v in task.__dict__.items() if not k.startswith('_')}
        return {
            "success": True,
            "operation": "complete",
            "task": task_dict
        }

    async def _list_tasks(self, session: AsyncSession, user_id: str) -> Dict[str, Any]:
        """List all tasks for a specific user"""
        statement = select(Task).where(Task.user_id == user_id)
        result = await session.exec(statement)
        tasks = result.all()

        # Convert tasks to a list of simplified dictionaries
        tasks_list = []
        for task in tasks:
            # Only include essential fields to reduce response size
            task_dict = {
                "id": str(task.id),
                "title": task.title,
                "description": task.description,
                "completed": task.completed
            }
            tasks_list.append(task_dict)

        return {
            "success": True,
            "operation": "list",
            "tasks": tasks_list
        }


# Global instance
todo_mcp_tool = TodoMCPTask()


def get_todo_mcp_tool():
    """Get the global todo MCP tool instance"""
    return todo_mcp_tool