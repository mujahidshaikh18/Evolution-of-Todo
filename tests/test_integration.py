"""
Integration tests for the Todo In-Memory Python Console App.
Tests the interaction between different components.
"""
import unittest
from src.todo_manager import TodoManager
from src.utils import format_task_list


class TestIntegration(unittest.TestCase):
    """Integration tests for the application components."""

    def test_full_crud_workflow(self):
        """Test the complete CRUD workflow."""
        manager = TodoManager()

        # Add tasks
        task1 = manager.add_task("First Task", "Description for first task")
        task2 = manager.add_task("Second Task")

        self.assertEqual(len(manager.list_tasks()), 2)
        self.assertEqual(task1.id, 1)
        self.assertEqual(task2.id, 2)

        # List tasks
        tasks = manager.list_tasks()
        self.assertEqual(len(tasks), 2)

        # Format task list for display
        formatted = format_task_list(tasks)
        self.assertIn("1. [ ] First Task - Description for first task", formatted)
        self.assertIn("2. [ ] Second Task - ", formatted)

        # Update a task
        success = manager.update_task(1, "Updated First Task", "Updated description")
        self.assertTrue(success)
        self.assertEqual(manager.get_task_by_id(1).title, "Updated First Task")
        self.assertEqual(manager.get_task_by_id(1).description, "Updated description")

        # Complete a task
        success = manager.toggle_complete(1)
        self.assertTrue(success)
        self.assertTrue(manager.get_task_by_id(1).completed)

        # Verify the formatted list reflects the changes
        updated_tasks = manager.list_tasks()
        updated_formatted = format_task_list(updated_tasks)
        self.assertIn("1. [x] Updated First Task - Updated description", updated_formatted)

        # Delete a task
        success = manager.delete_task(2)
        self.assertTrue(success)
        self.assertEqual(len(manager.list_tasks()), 1)
        self.assertIsNone(manager.get_task_by_id(2))

    def test_validation_integration(self):
        """Test that validation works across components."""
        manager = TodoManager()

        # Try to add a task with invalid title
        invalid_task = manager.add_task("", "Valid Description")  # Empty title
        self.assertIsNone(invalid_task)
        self.assertEqual(len(manager.list_tasks()), 0)

        # Try to add a task with invalid description
        invalid_task = manager.add_task("Valid Title", "A" * 1001)  # Too long description
        self.assertIsNone(invalid_task)
        self.assertEqual(len(manager.list_tasks()), 0)

        # Add a valid task
        valid_task = manager.add_task("Valid Title", "Valid Description")
        self.assertIsNotNone(valid_task)
        self.assertEqual(len(manager.list_tasks()), 1)

        # Try to update with invalid data
        success = manager.update_task(1, title="")  # Empty title
        self.assertFalse(success)

        success = manager.update_task(1, description="A" * 1001)  # Too long description
        self.assertFalse(success)

        # Verify the task is still valid
        task = manager.get_task_by_id(1)
        self.assertEqual(task.title, "Valid Title")
        self.assertEqual(task.description, "Valid Description")

    def test_id_generation_and_lookup(self):
        """Test ID generation and lookup across operations."""
        manager = TodoManager()

        # Add multiple tasks and verify IDs
        task1 = manager.add_task("Task 1")
        task2 = manager.add_task("Task 2")
        task3 = manager.add_task("Task 3")

        self.assertEqual(task1.id, 1)
        self.assertEqual(task2.id, 2)
        self.assertEqual(task3.id, 3)

        # Verify lookups work correctly
        self.assertIsNotNone(manager.get_task_by_id(1))
        self.assertEqual(manager.get_task_by_id(1).title, "Task 1")
        self.assertIsNotNone(manager.get_task_by_id(2))
        self.assertEqual(manager.get_task_by_id(2).title, "Task 2")
        self.assertIsNotNone(manager.get_task_by_id(3))
        self.assertEqual(manager.get_task_by_id(3).title, "Task 3")

        # Delete middle task and add new one
        manager.delete_task(2)
        task4 = manager.add_task("Task 4")

        self.assertEqual(task4.id, 4)
        self.assertIsNone(manager.get_task_by_id(2))  # Should be gone
        self.assertIsNotNone(manager.get_task_by_id(4))  # Should exist

        # Verify remaining tasks
        remaining_tasks = manager.list_tasks()
        self.assertEqual(len(remaining_tasks), 3)  # Tasks 1, 3, and 4
        self.assertIsNotNone(manager.get_task_by_id(1))
        self.assertIsNotNone(manager.get_task_by_id(3))
        self.assertIsNotNone(manager.get_task_by_id(4))

    def test_formatting_with_various_states(self):
        """Test formatting with different task states."""
        manager = TodoManager()

        # Add tasks with different states
        task1 = manager.add_task("Incomplete Task", "Description")
        task2 = manager.add_task("Complete Task", "Description")
        task3 = manager.add_task("Task Without Description")

        # Complete one task
        manager.toggle_complete(2)

        # Format and verify
        tasks = manager.list_tasks()
        formatted = format_task_list(tasks)

        self.assertIn("1. [ ] Incomplete Task - Description", formatted)
        self.assertIn("2. [x] Complete Task - Description", formatted)
        self.assertIn("3. [ ] Task Without Description - ", formatted)

        # Update task without description to have one
        manager.update_task(3, description="Added description")
        updated_tasks = manager.list_tasks()
        updated_formatted = format_task_list(updated_tasks)

        self.assertIn("3. [ ] Task Without Description - Added description", updated_formatted)


if __name__ == "__main__":
    unittest.main()