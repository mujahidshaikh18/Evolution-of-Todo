# Todo In-Memory Python Console App - Phase I

A simple command-line todo application with in-memory storage that allows users to perform basic CRUD operations on tasks.

## Features

- **Add Tasks**: Create new todo items with required title and optional description
- **View Tasks**: Display all tasks with ID, title, status (✓/✗), and description
- **Update Tasks**: Modify existing task title or description
- **Complete Tasks**: Toggle task completion status (complete ↔ incomplete)
- **Delete Tasks**: Remove tasks by ID
- **In-Memory Storage**: Tasks persist during session, lost on exit (as designed)

## Prerequisites

- Python 3.13+
- UV package manager (optional, for dependency management)

## Installation

1. Clone or download the repository
2. Navigate to the project directory
3. The application is ready to run (no installation required for this in-memory version)

## Usage

To run the application:

```bash
python src/main.py
```

## Available Commands

- `add` - Add a new task (prompts for title and description)
- `list` - List all tasks with ID, title, status, and description
- `complete <id>` - Toggle completion status of task with specified ID
- `update <id>` - Update task title or description by ID
- `delete <id>` - Delete task by ID
- `help` - Show command menu
- `exit` - Quit the application

## Example Usage

1. Start the application: `python src/main.py`
2. Add a task: Enter `add` and follow prompts
3. List tasks: Enter `list` to see all tasks
4. Complete a task: Enter `complete 1` (where 1 is the task ID)
5. Exit: Enter `exit` to quit

## Project Structure

```
todo-phase1/
├── src/
│   ├── __init__.py
│   ├── main.py              # Entry point, CLI menu loop
│   ├── task.py              # Task dataclass/model
│   ├── todo_manager.py      # Business logic (CRUD operations)
│   └── utils.py             # Input validation, formatters
├── specs/
│   └── 001-phase1-cli/      # Specification files
├── README.md
├── pyproject.toml
└── .gitignore
```

## Technology Stack

- **Language**: Python 3.13+
- **Architecture**: Clean architecture with separation of concerns
- **Storage**: In-memory List[Task] (no file/database storage)
- **Interface**: Command-line only
- **Dependencies**: Standard library only (no external dependencies)

## Development

This project follows a spec-driven development approach with the following phases:

1. **Specification**: Requirements captured in specs/
2. **Planning**: Architecture decisions in specs/001-phase1-cli/plan.md
3. **Tasks**: Implementation tasks in specs/001-phase1-cli/tasks.md
4. **Implementation**: Source code in src/

## Testing

The application includes a comprehensive test suite with 36 tests covering all functionality:

### Running Tests

To run all tests:
```bash
python -m unittest discover tests -v
```

To run specific test files:
```bash
python -m unittest tests.test_task -v          # Task-related tests
python -m unittest tests.test_todo_manager -v  # TodoManager tests
python -m unittest tests.test_utils -v         # Utility function tests
python -m unittest tests.test_integration -v   # Integration tests
```

See TESTING.md for detailed instructions on running tests.

## Validation

All 5 basic features have been manually validated:
- ✅ Add Task
- ✅ View Task List
- ✅ Update Task
- ✅ Mark as Complete
- ✅ Delete Task
- ✅ Error handling for invalid inputs
- ✅ Input validation (title length: 1-200 chars, description max 1000 chars)