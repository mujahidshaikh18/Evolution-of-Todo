# Quickstart Guide: Todo In-Memory Python Console App - Phase I

**Date**: 2026-01-02
**Feature**: Todo In-Memory Python Console App - Phase I
**Plan**: [Implementation Plan](plan.md)

## Setup Instructions

### Prerequisites
- Python 3.13+ installed on your system
- UV package manager installed

### Environment Setup
1. Clone or create the project directory
2. Navigate to the project root
3. Install dependencies using UV:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install --requirement requirements.txt
   ```

### Project Structure
```
todo-phase1/
├── src/
│   ├── __init__.py
│   ├── main.py              # Entry point, CLI menu loop
│   ├── task.py              # Task dataclass/model
│   ├── todo_manager.py      # Business logic (CRUD operations)
│   └── utils.py             # Input validation, formatters
├── specs/
│   ├── 001-phase1-cli/      # Current feature specs
│   │   ├── spec.md
│   │   ├── plan.md
│   │   ├── research.md
│   │   ├── data-model.md
│   │   └── quickstart.md
└── pyproject.toml           # UV configuration
```

## Running the Application

### Direct Execution
```bash
python src/main.py
```

### Expected Behavior
- Application starts and displays welcome message
- Shows command menu
- Enters command loop waiting for user input
- Processes commands until 'exit' is entered

## Available Commands

### add
- **Purpose**: Create a new task
- **Usage**: `add`
- **Flow**: Prompts for title (required), then description (optional)
- **Output**: Displays confirmation with new task ID

### list
- **Purpose**: Display all tasks
- **Usage**: `list`
- **Output**: Shows all tasks with ID, title, status (✓/✗), and description

### complete <id>
- **Purpose**: Toggle task completion status
- **Usage**: `complete 1` (where 1 is the task ID)
- **Output**: Confirms status change

### update <id>
- **Purpose**: Modify existing task title/description
- **Usage**: `update 1` (where 1 is the task ID)
- **Flow**: Prompts for new title/description
- **Output**: Confirms update

### delete <id>
- **Purpose**: Remove task by ID
- **Usage**: `delete 1` (where 1 is the task ID)
- **Output**: Confirms deletion

### help
- **Purpose**: Show command menu
- **Usage**: `help`
- **Output**: Displays available commands

### exit
- **Purpose**: Quit the application
- **Usage**: `exit`
- **Output**: Application terminates

## Development Workflow

### 1. Task Model Development
- Implement Task dataclass in `src/task.py`
- Add validation methods for title/description
- Test dataclass functionality

### 2. Business Logic Development
- Implement TodoManager class in `src/todo_manager.py`
- Add CRUD operations (add_task, delete_task, etc.)
- Test operations with in-memory storage

### 3. CLI Interface Development
- Implement command parsing in `src/main.py`
- Add user interaction loops
- Connect CLI to business logic

### 4. Utilities Development
- Add validation functions in `src/utils.py`
- Create formatting helpers
- Implement error handling utilities

## Testing Commands

After implementation, verify functionality with these manual tests:

### Add Task Tests
- Run: `add` → Enter "Test Title" → Enter "Test Description"
- Expected: Task created with ID 1, displayed confirmation

### List Tasks Tests
- Run: `list` after adding tasks
- Expected: All tasks displayed with proper formatting

### Complete Task Tests
- Run: `complete 1` (with existing task ID)
- Expected: Task status toggles, reflected in list

### Error Handling Tests
- Run: `complete 999` (non-existent ID)
- Expected: Clear error message, no crash

## Common Issues and Solutions

### Python Version Issues
- **Problem**: Application fails to run
- **Solution**: Verify Python 3.13+ is installed and active

### Import Errors
- **Problem**: "Module not found" errors
- **Solution**: Ensure you're running from project root directory

### Invalid Input Handling
- **Problem**: Application crashes on invalid input
- **Solution**: All user inputs should be validated before processing