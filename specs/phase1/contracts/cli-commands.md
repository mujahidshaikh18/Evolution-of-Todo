# CLI Command Contracts: Todo In-Memory Python Console App - Phase I

**Date**: 2026-01-02
**Feature**: Todo In-Memory Python Console App - Phase I
**Plan**: [Implementation Plan](../plan.md)

## Command Interface Specification

### add Command
- **Purpose**: Create a new task
- **Input**: None (interactive prompt for title and description)
- **Output**: Confirmation message with new task ID
- **Success Criteria**: Task created with unique ID and added to in-memory list
- **Error Cases**: Invalid input (empty title, title too long) → error message

### list Command
- **Input**: None
- **Output**: Formatted list of all tasks with ID, title, status (✓/✗), and description
- **Success Criteria**: All tasks displayed in readable format
- **Error Cases**: No tasks → "No tasks found" message

### complete <id> Command
- **Input**: Task ID (integer)
- **Output**: Confirmation of status change
- **Success Criteria**: Task status toggled (complete ↔ incomplete)
- **Error Cases**: Invalid ID → error message

### update <id> Command
- **Input**: Task ID (integer), new title/description (interactive)
- **Output**: Confirmation of update
- **Success Criteria**: Task properties updated in memory
- **Error Cases**: Invalid ID → error message

### delete <id> Command
- **Input**: Task ID (integer)
- **Output**: Confirmation of deletion
- **Success Criteria**: Task removed from in-memory list
- **Error Cases**: Invalid ID → error message

### help Command
- **Input**: None
- **Output**: List of available commands with brief descriptions
- **Success Criteria**: Command menu displayed to user

### exit Command
- **Input**: None
- **Output**: None (application terminates)
- **Success Criteria**: Clean application shutdown

## Data Validation Contracts

### Title Validation
- **Input**: String
- **Validation**: Length 1-200 characters
- **Output**: Boolean (valid/invalid)

### Description Validation
- **Input**: String (optional)
- **Validation**: Length 0-1000 characters
- **Output**: Boolean (valid/invalid)

### ID Validation
- **Input**: String (to be converted to integer)
- **Validation**: Must be integer within valid task ID range
- **Output**: Boolean (valid/invalid)

## Error Response Format
- **Format**: "Error: [descriptive message]"
- **Purpose**: Clear, user-friendly error messages
- **Examples**:
  - "Error: Task with ID 5 not found"
  - "Error: Title must be between 1 and 200 characters"

## Success Response Format
- **Format**: "[Action] successful: [descriptive message]"
- **Purpose**: Clear confirmation of successful operations
- **Examples**:
  - "Task added successfully: ID 1"
  - "Task 1 updated successfully"