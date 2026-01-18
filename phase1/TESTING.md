# Testing Documentation for Todo CLI App

## How to Run Tests

The Todo CLI App comes with a comprehensive test suite. Here's how to run the tests:

### Prerequisites
- Python 3.13+ installed on your system
- The application files in the correct directory structure

### Running All Tests

To run all tests at once, use the following command from the project root directory:

```bash
python -m unittest discover tests -v
```

This will run all 36 tests across all test files and show you detailed output.

### Running Individual Test Files

You can run individual test files separately:

```bash
# Run task-related tests
python -m unittest tests.test_task -v

# Run TodoManager tests
python -m unittest tests.test_todo_manager -v

# Run utility function tests
python -m unittest tests.test_utils -v

# Run integration tests
python -m unittest tests.test_integration -v
```

### Running Specific Test Cases

To run a specific test method:

```bash
# Run a specific test
python -m unittest tests.test_task.TestTask.test_task_creation -v

# Example: Run the test that checks task creation
python -m unittest tests.test_todo_manager.TestTodoManager.test_add_task_success -v
```

### Test Directory Structure

The tests are organized in the `tests/` directory:

```
tests/
├── test_task.py          # Tests for Task dataclass and validation
├── test_todo_manager.py  # Tests for TodoManager CRUD operations
├── test_utils.py         # Tests for utility functions (validation, formatting)
└── test_integration.py   # Integration tests for full workflows
```

### What Each Test File Covers

1. **test_task.py**:
   - Task creation with valid/invalid parameters
   - Title and description validation methods
   - Default values for optional fields

2. **test_todo_manager.py**:
   - All CRUD operations (Add, List, Update, Delete, Complete)
   - ID generation and management
   - Error handling for invalid inputs
   - Task lookup by ID

3. **test_utils.py**:
   - Validation functions for titles and descriptions
   - Task list formatting functionality
   - Edge cases for empty lists and tasks

4. **test_integration.py**:
   - Full workflow tests combining multiple operations
   - Integration between different components
   - End-to-end scenarios

### Test Results

When you run the tests, you'll see output like:
```
test_add_task_success (tests.test_todo_manager.TestTodoManager.test_add_task_success)
Test adding a valid task. ... ok
```

- `ok` means the test passed
- `FAIL` means the test failed
- `ERROR` means there was an unexpected error

All 36 tests should pass if the application is working correctly.