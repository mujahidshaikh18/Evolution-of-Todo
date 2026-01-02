"""
Task dataclass for the Todo In-Memory Python Console App.

This module defines the Task entity with fields, validation, and creation logic.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Task:
    """
    Represents a single todo item with properties including ID (unique identifier),
    title (required string), description (optional string), completion status (boolean),
    and creation timestamp.
    """
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
    created_at: datetime = None

    def __post_init__(self):
        """Initialize the created_at field if not provided."""
        if self.created_at is None:
            self.created_at = datetime.now()

    @staticmethod
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

    @staticmethod
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