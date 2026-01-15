# Data Model: Todo In-Memory Python Console App - Phase I

**Date**: 2026-01-02
**Feature**: Todo In-Memory Python Console App - Phase I
**Plan**: [Implementation Plan](plan.md)

## Task Entity

### Fields
- **id**: int (unique, auto-generated, sequential starting from 1)
- **title**: str (required, 1-200 characters)
- **description**: str (optional, max 1000 characters)
- **completed**: bool (default False)
- **created_at**: datetime (auto-generated on creation)

### Validation Rules
- **title**: Required field, length between 1-200 characters (inclusive)
- **description**: Optional field, maximum 1000 characters if provided
- **completed**: Boolean value, defaults to False when creating new tasks
- **id**: Auto-incremented integer, unique within current session

### State Transitions
- **Status**: Incomplete (False) ↔ Complete (True) via toggle operation
- **Lifecycle**: Created → Active → Completed/Deleted

## TaskList Collection

### Structure
- **Storage**: List[Task] (in-memory)
- **Ordering**: Preserves creation order (FIFO)
- **Session-bound**: Lost on application exit (as specified in requirements)

### Operations
- **Add**: Append new Task to end of list
- **Find**: Linear search by ID (acceptable for small lists)
- **Update**: Modify Task properties in-place
- **Delete**: Remove Task from list by index
- **List**: Iterate through all Tasks for display