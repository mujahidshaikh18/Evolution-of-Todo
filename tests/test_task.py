"""
Unit tests for the Task dataclass in the Todo In-Memory Python Console App.
"""
import unittest
from datetime import datetime
from src.task import Task


class TestTask(unittest.TestCase):
    """Test cases for the Task dataclass."""

    def test_task_creation(self):
        """Test creating a task with valid parameters."""
        task = Task(id=1, title="Test Task", description="Test Description")

        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertFalse(task.completed)
        self.assertIsInstance(task.created_at, datetime)

    def test_task_creation_optional_description(self):
        """Test creating a task with only required parameters."""
        task = Task(id=1, title="Test Task")

        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Task")
        self.assertIsNone(task.description)
        self.assertFalse(task.completed)

    def test_task_default_values(self):
        """Test default values for optional fields."""
        task = Task(id=1, title="Test Task")

        self.assertFalse(task.completed)
        self.assertIsNone(task.description)

    def test_validate_title_valid(self):
        """Test title validation with valid input."""
        valid_titles = [
            "A",  # Minimum length
            "A" * 200,  # Maximum length
            "Valid Title 123!@#",  # Mixed content
        ]

        for title in valid_titles:
            with self.subTest(title=title):
                self.assertTrue(Task.validate_title(title))

    def test_validate_title_invalid(self):
        """Test title validation with invalid input."""
        invalid_titles = [
            "",  # Empty
            "A" * 201,  # Too long
            123,  # Not a string
        ]

        for title in invalid_titles:
            with self.subTest(title=title):
                self.assertFalse(Task.validate_title(title))

    def test_validate_description_valid(self):
        """Test description validation with valid input."""
        valid_descriptions = [
            None,  # Optional field
            "",  # Empty string
            "A",  # Minimum content
            "A" * 1000,  # Maximum length
        ]

        for desc in valid_descriptions:
            with self.subTest(desc=desc):
                self.assertTrue(Task.validate_description(desc))

    def test_validate_description_invalid(self):
        """Test description validation with invalid input."""
        invalid_descriptions = [
            "A" * 1001,  # Too long
            123,  # Not a string
        ]

        for desc in invalid_descriptions:
            with self.subTest(desc=desc):
                self.assertFalse(Task.validate_description(desc))


if __name__ == "__main__":
    unittest.main()