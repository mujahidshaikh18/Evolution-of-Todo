"""
Main CLI interface for the Todo In-Memory Python Console App.

This module provides the command-line interface for interacting with tasks.
"""
import sys
from typing import Optional

# Handle both direct execution and module import
try:
    from .todo_manager import TodoManager
    from .utils import format_task_list
except ImportError:
    # When running directly, import from the same directory
    from todo_manager import TodoManager
    from utils import format_task_list


def display_menu():
    """Display the command menu to the user."""
    print("\n" + "="*50)
    print("           TODO CLI APPLICATION")
    print("="*50)
    print("Available commands:")
    print("  1. add              - Add a new task")
    print("  2. list             - List all tasks")
    print("  3. complete <id>    - Mark task as complete/incomplete")
    print("  4. update <id>      - Update task title/description")
    print("  5. delete <id>      - Delete a task")
    print("  6. help             - Show this menu")
    print("  7. exit             - Exit the application")
    print("="*50)
    print("You can also type the command number (1-7) instead of the full command name.\n")


def get_user_input(prompt: str) -> str:
    """
    Get input from the user with a prompt.

    Args:
        prompt: The prompt to display to the user

    Returns:
        The user's input as a string
    """
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print("\nExiting application...")
        sys.exit(0)


def parse_command(user_input: str) -> tuple:
    """
    Parse user input into command and arguments.

    Args:
        user_input: The raw user input

    Returns:
        A tuple containing the command and arguments
    """
    parts = user_input.strip().split()
    if not parts:
        return "", []

    command = parts[0].lower()
    args = parts[1:]

    # Convert command numbers to command names
    command_map = {
        '1': 'add',
        '2': 'list',
        '3': 'complete',
        '4': 'update',
        '5': 'delete',
        '6': 'help',
        '7': 'exit'
    }

    if command in command_map:
        command = command_map[command]

    return command, args


def main():
    """Main application loop."""
    try:
        print("╔" + "═" * 48 + "╗")
        print("║           WELCOME TO TODO CLI APP           ║")
        print("╚" + "═" * 48 + "╝")
    except UnicodeEncodeError:
        print("=" * 50)
        print("         WELCOME TO TODO CLI APP         ")
        print("=" * 50)

    display_menu()

    todo_manager = TodoManager()

    while True:
        user_input = get_user_input("Enter your choice (command or number 1-7): ")
        command, args = parse_command(user_input)

        if command == "add":
            print("\n📝 Adding a new task...")
            # Get title from user
            title = get_user_input("Enter task title (required): ")
            if not title:
                print("❌ Error: Title is required and cannot be empty.")
                continue

            # Get description from user (optional)
            description = get_user_input("Enter task description (optional, press Enter to skip): ")
            if not description:  # If user just pressed Enter, set to None
                description = None

            # Add the task
            task = todo_manager.add_task(title, description)
            if task:
                print(f"✅ Task added successfully: ID {task.id}")
            else:
                print("❌ Error: Invalid input. Title must be 1-200 characters, description max 1000 characters.")

        elif command == "list":
            print("\n📋 Your tasks:")
            tasks = todo_manager.list_tasks()
            formatted_tasks = format_task_list(tasks)
            print(formatted_tasks)
            print(f"Total tasks: {len(tasks)}")

        elif command in ["complete", "toggle"]:
            if not args:
                print("❌ Error: Please provide a task ID. Usage: complete <id> or 3 <id>")
                continue

            try:
                task_id = int(args[0])
                success = todo_manager.toggle_complete(task_id)
                if success:
                    task = todo_manager.get_task_by_id(task_id)
                    status = "✅ complete" if task.completed else "❌ incomplete"
                    print(f"✅ Task {task_id} marked as {status}.")
                else:
                    print(f"❌ Error: Task with ID {task_id} not found.")
            except ValueError:
                print("❌ Error: Task ID must be a number.")

        elif command == "update":
            if not args:
                print("❌ Error: Please provide a task ID. Usage: update <id> or 4 <id>")
                continue

            try:
                task_id = int(args[0])
                task = todo_manager.get_task_by_id(task_id)
                if not task:
                    print(f"❌ Error: Task with ID {task_id} not found.")
                    continue

                print(f"Updating task {task_id}: '{task.title}'")
                # Get new title (optional)
                new_title_input = get_user_input(f"Enter new title (current: '{task.title}', press Enter to keep current): ")
                if new_title_input == "":  # If user just pressed Enter, keep current title
                    new_title = None
                else:
                    new_title = new_title_input

                # Get new description (optional)
                new_desc_input = get_user_input(f"Enter new description (current: '{task.description or 'None'}', press Enter to keep current): ")
                if new_desc_input == "":  # If user just pressed Enter, keep current description
                    new_desc = None
                else:
                    new_desc = new_desc_input

                success = todo_manager.update_task(task_id, new_title, new_desc)
                if success:
                    print(f"✅ Task {task_id} updated successfully.")
                else:
                    print("❌ Error: Invalid input. Title must be 1-200 characters, description max 1000 characters.")
            except ValueError:
                print("❌ Error: Task ID must be a number.")

        elif command == "delete":
            if not args:
                print("❌ Error: Please provide a task ID. Usage: delete <id> or 5 <id>")
                continue

            try:
                task_id = int(args[0])
                success = todo_manager.delete_task(task_id)
                if success:
                    print(f"✅ Task {task_id} deleted successfully.")
                else:
                    print(f"❌ Error: Task with ID {task_id} not found.")
            except ValueError:
                print("❌ Error: Task ID must be a number.")

        elif command in ["help", "?"]:
            display_menu()

        elif command in ["exit", "quit"]:
            try:
                print("\n" + "═" * 50)
                print("Thank you for using the Todo CLI App! Goodbye! 👋")
                print("═" * 50)
            except UnicodeEncodeError:
                print("\n" + "=" * 50)
                print("Thank you for using the Todo CLI App! Goodbye! :)")
                print("=" * 50)
            break

        else:
            if command:
                print(f"❌ Unknown command: '{command}'. Type 'help' or '6' for available commands.")
            else:
                # Empty input - just show the menu again
                continue


if __name__ == "__main__":
    main()