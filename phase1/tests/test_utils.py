"""
Unit tests for the utils module in the Todo In-Memory Python Console App.
"""
import unittest
from src.utils import validate_title, validate_description, format_task_list
from src.task import Task


class TestUtils(unittest.TestCase):
    """Test cases for utility functions."""

    def test_validate_title_valid(self):
        """Test title validation with valid input."""
        valid_titles = [
            "A",  # Minimum length
            "A" * 200,  # Maximum length
            "Valid Title 123!@#",  # Mixed content
        ]

        for title in valid_titles:
            with self.subTest(title=title):
                self.assertTrue(validate_title(title))

    def test_validate_title_invalid(self):
        """Test title validation with invalid input."""
        invalid_titles = [
            "",  # Empty
            "A" * 201,  # Too long
            123,  # Not a string
        ]

        for title in invalid_titles:
            with self.subTest(title=title):
                self.assertFalse(validate_title(title))

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
                self.assertTrue(validate_description(desc))

    def test_validate_description_invalid(self):
        """Test description validation with invalid input."""
        invalid_descriptions = [
            "A" * 1001,  # Too long
            123,  # Not a string
        ]

        for desc in invalid_descriptions:
            with self.subTest(desc=desc):
                self.assertFalse(validate_description(desc))

    def test_format_task_list_empty(self):
        """Test formatting an empty task list."""
        result = format_task_list([])
        self.assertEqual(result, "No tasks found.")

    def test_format_task_list_single_task_incomplete(self):
        """Test formatting a single incomplete task."""
        task = Task(id=1, title="Test Task", description="Test Description")
        result = format_task_list([task])
        expected = "1. [ ] Test Task - Test Description"
        self.assertEqual(result, expected)

    def test_format_task_list_single_task_complete(self):
        """Test formatting a single complete task."""
        task = Task(id=1, title="Test Task", description="Test Description", completed=True)
        result = format_task_list([task])
        expected = "1. [x] Test Task - Test Description"
        self.assertEqual(result, expected)

    def test_format_task_list_multiple_tasks(self):
        """Test formatting multiple tasks."""
        task1 = Task(id=1, title="Task 1", description="Description 1", completed=False)
        task2 = Task(id=2, title="Task 2", description="Description 2", completed=True)
        task3 = Task(id=3, title="Task 3", description=None, completed=False)

        result = format_task_list([task1, task2, task3])
        expected = "1. [ ] Task 1 - Description 1\n2. [x] Task 2 - Description 2\n3. [ ] Task 3 - "
        self.assertEqual(result, expected)

    def test_format_task_list_task_without_description(self):
        """Test formatting a task without description."""
        task = Task(id=1, title="Test Task", description=None)
        result = format_task_list([task])
        expected = "1. [ ] Test Task - "
        self.assertEqual(result, expected)

    def test_format_task_list_task_with_empty_description(self):
        """Test formatting a task with empty description."""
        task = Task(id=1, title="Test Task", description="")
        result = format_task_list([task])
        expected = "1. [ ] Test Task - "
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()