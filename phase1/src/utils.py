"""
Utility functions for the Todo In-Memory Python Console App.

This module provides validation and formatting utilities.
"""
from typing import List, Optional

# Handle both direct execution and module import
try:
    from .task import Task
except ImportError:
    # When running directly, import from the same directory
    from task import Task


def validate_title(title: str) -> bool:
    """
    Validate title length (1-200 characters).

    Args:
        title: The title to validate

    Returns:
        True if valid, False otherwise
    """
    if not isinstance(title, str):
        return False
    return 1 <= len(title) <= 200


def validate_description(description: Optional[str]) -> bool:
    """
    Validate description length (max 1000 characters if provided).

    Args:
        description: The description to validate

    Returns:
        True if valid, False otherwise
    """
    if description is None:
        return True
    if not isinstance(description, str):
        return False
    return len(description) <= 1000


def format_task_list(tasks: List[Task]) -> str:
    """
    Format a list of tasks for display with ID, title, status ([x]/[ ]), and description.

    Args:
        tasks: List of Task objects to format

    Returns:
        Formatted string representation of the tasks
    """
    if not tasks:
        return "No tasks found."

    formatted_tasks = []
    for task in tasks:
        status = "[x]" if task.completed else "[ ]"
        if task.description is not None:
            description = task.description
        else:
            description = ""
        formatted_task = f"{task.id}. {status} {task.title} - {description}"
        formatted_tasks.append(formatted_task)

    return "\n".join(formatted_tasks)