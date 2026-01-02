"""
Unit tests for the TodoManager class in the Todo In-Memory Python Console App.
"""
import unittest
from src.todo_manager import TodoManager
from src.task import Task


class TestTodoManager(unittest.TestCase):
    """Test cases for the TodoManager class."""

    def test_initialization(self):
        """Test TodoManager initialization."""
        manager = TodoManager()

        self.assertEqual(len(manager.tasks), 0)
        self.assertEqual(manager._next_id, 1)

    def test_add_task_success(self):
        """Test adding a valid task."""
        manager = TodoManager()
        task = manager.add_task("Test Title", "Test Description")

        self.assertIsNotNone(task)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Title")
        self.assertEqual(task.description, "Test Description")
        self.assertFalse(task.completed)
        self.assertEqual(len(manager.tasks), 1)

    def test_add_task_without_description(self):
        """Test adding a task without description."""
        manager = TodoManager()
        task = manager.add_task("Test Title")

        self.assertIsNotNone(task)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Title")
        self.assertIsNone(task.description)
        self.assertEqual(len(manager.tasks), 1)

    def test_add_task_invalid_title(self):
        """Test adding a task with invalid title."""
        manager = TodoManager()

        # Test empty title
        task = manager.add_task("")
        self.assertIsNone(task)

        # Test title too long
        task = manager.add_task("A" * 201)
        self.assertIsNone(task)

        # Test title too short (empty)
        task = manager.add_task("")
        self.assertIsNone(task)

        self.assertEqual(len(manager.tasks), 0)

    def test_add_task_invalid_description(self):
        """Test adding a task with invalid description."""
        manager = TodoManager()

        # Test description too long
        task = manager.add_task("Valid Title", "A" * 1001)
        self.assertIsNone(task)

        self.assertEqual(len(manager.tasks), 0)

    def test_list_tasks(self):
        """Test listing all tasks."""
        manager = TodoManager()
        manager.add_task("Task 1")
        manager.add_task("Task 2", "Description for Task 2")

        tasks = manager.list_tasks()

        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].title, "Task 1")
        self.assertEqual(tasks[1].title, "Task 2")

    def test_get_task_by_id(self):
        """Test retrieving a task by its ID."""
        manager = TodoManager()
        task1 = manager.add_task("Task 1")
        task2 = manager.add_task("Task 2")

        retrieved_task = manager.get_task_by_id(1)
        self.assertIsNotNone(retrieved_task)
        self.assertEqual(retrieved_task.id, 1)
        self.assertEqual(retrieved_task.title, "Task 1")

        retrieved_task = manager.get_task_by_id(2)
        self.assertIsNotNone(retrieved_task)
        self.assertEqual(retrieved_task.id, 2)
        self.assertEqual(retrieved_task.title, "Task 2")

        retrieved_task = manager.get_task_by_id(999)
        self.assertIsNone(retrieved_task)

    def test_update_task_success(self):
        """Test updating a task successfully."""
        manager = TodoManager()
        task = manager.add_task("Original Title", "Original Description")

        # Update both title and description
        success = manager.update_task(1, "Updated Title", "Updated Description")
        self.assertTrue(success)
        self.assertEqual(task.title, "Updated Title")
        self.assertEqual(task.description, "Updated Description")

    def test_update_task_partial(self):
        """Test updating only title or description."""
        manager = TodoManager()
        task = manager.add_task("Original Title", "Original Description")

        # Update only title
        success = manager.update_task(1, title="Updated Title")
        self.assertTrue(success)
        self.assertEqual(task.title, "Updated Title")
        self.assertEqual(task.description, "Original Description")

        # Update only description
        task2 = manager.add_task("Another Title", "Another Description")
        success = manager.update_task(2, description="New Description")
        self.assertTrue(success)
        self.assertEqual(task2.title, "Another Title")
        self.assertEqual(task2.description, "New Description")

    def test_update_task_invalid_input(self):
        """Test updating a task with invalid input."""
        manager = TodoManager()
        manager.add_task("Original Title")

        # Try to update with invalid title
        success = manager.update_task(1, title="A" * 201)
        self.assertFalse(success)

        # Try to update with invalid description
        success = manager.update_task(1, description="A" * 1001)
        self.assertFalse(success)

        # Try to update non-existent task
        success = manager.update_task(999, title="New Title")
        self.assertFalse(success)

    def test_delete_task_success(self):
        """Test deleting a task successfully."""
        manager = TodoManager()
        manager.add_task("Task 1")
        manager.add_task("Task 2")

        self.assertEqual(len(manager.tasks), 2)

        success = manager.delete_task(1)
        self.assertTrue(success)
        self.assertEqual(len(manager.tasks), 1)
        self.assertIsNone(manager.get_task_by_id(1))

    def test_delete_task_nonexistent(self):
        """Test deleting a non-existent task."""
        manager = TodoManager()
        manager.add_task("Task 1")

        success = manager.delete_task(999)
        self.assertFalse(success)
        self.assertEqual(len(manager.tasks), 1)

    def test_toggle_complete_success(self):
        """Test toggling a task's completion status."""
        manager = TodoManager()
        task = manager.add_task("Test Task")

        # Initially incomplete
        self.assertFalse(task.completed)

        # Toggle to complete
        success = manager.toggle_complete(1)
        self.assertTrue(success)
        self.assertTrue(task.completed)

        # Toggle back to incomplete
        success = manager.toggle_complete(1)
        self.assertTrue(success)
        self.assertFalse(task.completed)

    def test_toggle_complete_nonexistent(self):
        """Test toggling completion for non-existent task."""
        manager = TodoManager()
        manager.add_task("Test Task")

        success = manager.toggle_complete(999)
        self.assertFalse(success)

    def test_sequential_id_generation(self):
        """Test that task IDs are generated sequentially."""
        manager = TodoManager()

        task1 = manager.add_task("Task 1")
        task2 = manager.add_task("Task 2")
        task3 = manager.add_task("Task 3")

        self.assertEqual(task1.id, 1)
        self.assertEqual(task2.id, 2)
        self.assertEqual(task3.id, 3)

        # Delete task in middle and add new one
        manager.delete_task(2)
        task4 = manager.add_task("Task 4")
        self.assertEqual(task4.id, 4)  # Should continue the sequence


if __name__ == "__main__":
    unittest.main()