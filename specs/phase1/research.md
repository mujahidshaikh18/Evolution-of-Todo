# Research: Todo In-Memory Python Console App - Phase I

**Date**: 2026-01-02
**Feature**: Todo In-Memory Python Console App - Phase I
**Plan**: [Implementation Plan](plan.md)

## Decision: Task ID Generation
**Rationale**: Sequential integers chosen for task IDs to make CLI interaction easier for users (typing "1", "2", "3" vs long UUID strings). IDs will be generated sequentially starting from 1, incrementing with each new task. IDs will reset to 1 when the application restarts (as expected for in-memory storage).
**Alternatives considered**:
- UUID strings: More complex for CLI users to type
- Timestamp-based IDs: More complex to implement and less intuitive

## Decision: Data Storage Structure
**Rationale**: Using List[Task] for in-memory storage as it preserves order and is simpler to implement for the scope of this application. For a small todo app with limited tasks, linear search performance is acceptable.
**Alternatives considered**:
- Dict[id, Task]: Faster lookups but doesn't preserve insertion order
- Separate ID counter: More complex implementation without significant benefit

## Decision: Task Model Implementation
**Rationale**: Using Python dataclass for the Task model to keep dependencies minimal while providing clean structure and type hints. Dataclasses provide automatic generation of special methods like __init__, __repr__, etc.
**Alternatives considered**:
- Pydantic BaseModel: More robust validation but adds external dependency
- Regular class: More verbose implementation of basic functionality

## Decision: Status Display Format
**Rationale**: Using ✓ / ✗ symbols for task completion status as they provide clear visual indication of completion status that's immediately recognizable.
**Alternatives considered**:
- Text: "Complete" / "Incomplete": Takes more space and is less visually distinct
- Checkbox: [x] / [ ]: Good but symbols are more concise

## Decision: Command Parsing Method
**Rationale**: Using manual string parsing (simple split) for Phase I to maintain minimal dependencies and simplicity. For a simple CLI app with few commands, this approach is sufficient.
**Alternatives considered**:
- argparse library: More robust but adds complexity for simple use case
- Click library: More features but violates "minimal dependencies" requirement