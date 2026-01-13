"""
TodoManager class for the Todo In-Memory Python Console App.

This module handles business logic for CRUD operations on tasks with in-memory storage.
"""
from typing import List, Optional

# Handle both direct execution and module import
try:
    from .task import Task
except ImportError:
    # When running directly, import from the same directory
    from task import Task


class TodoManager:
    """
    Manages in-memory storage and operations for tasks.
    Uses a List[Task] to store tasks with sequential ID generation.
    """
    def __init__(self):
        """Initialize the TodoManager with an empty task list and ID counter."""
        self.tasks: List[Task] = []
        self._next_id = 1

    def add_task(self, title: str, description: Optional[str] = None) -> Optional[Task]:
        """
        Add a new task with validation and unique ID generation.

        Args:
            title: Required title (1-200 characters)
            description: Optional description (max 1000 characters)

        Returns:
            The created Task object if successful, None otherwise
        """
        # Use Task's validation methods
        if not Task.validate_title(title):
            return None
        if not Task.validate_description(description):
            return None

        # Create task with unique ID
        task = Task(
            id=self._next_id,
            title=title,
            description=description,
            completed=False
        )
        self.tasks.append(task)
        self._next_id += 1
        return task

    def list_tasks(self) -> List[Task]:
        """
        Retrieve all tasks.

        Returns:
            List of all tasks
        """
        return self.tasks

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Find a task by its ID.

        Args:
            task_id: The ID of the task to find

        Returns:
            The Task object if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Update an existing task's title or description.

        Args:
            task_id: ID of the task to update
            title: New title (optional)
            description: New description (optional)

        Returns:
            True if update successful, False otherwise
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False

        if title is not None:
            if not Task.validate_title(title):
                return False
            task.title = title

        if description is not None:
            if not Task.validate_description(description):
                return False
            task.description = description

        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id: ID of the task to delete

        Returns:
            True if deletion successful, False otherwise
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False

        self.tasks.remove(task)
        return True

    def toggle_complete(self, task_id: int) -> bool:
        """
        Toggle the completion status of a task.

        Args:
            task_id: ID of the task to toggle

        Returns:
            True if toggle successful, False otherwise
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False

        task.completed = not task.completed
        return True