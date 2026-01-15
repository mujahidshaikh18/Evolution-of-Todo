---
id: 1
title: Todo Console App Constitution
stage: constitution
date: 2026-01-02
surface: agent
model: Claude Sonnet 4.5
feature: none
branch: master
user: user
command: sp.constitution
labels: [constitution, python, cli, todo]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
  - none
---

## Prompt

Project: Todo In-Memory Python Console App (Phase I - Hackathon II)

Core Principles:
- Spec-Driven Development:
- Simplicity First: In-memory storage, console interface, minimal dependencies
- Clean Architecture: Clear separation of concerns (data models, business logic, UI)
- User-Centric Design: Intuitive command-line interface with clear feedback
- Iterative Refinement: Refine specs until Claude Code generates correct implementation

Key Standards:
- Python version: 3.13+ (strict requirement)
- Package manager: UV (required for dependency management)
- Code style: PEP 8 compliant, type hints mandatory
- Project structure:
  - /src folder for all source code
  - /specs folder for all specification files
  - README.md with setup instructions
  - CLAUDE.md with Claude Code workflow instructions
- Naming conventions:
  - Snake_case for functions and variables
  - PascalCase for classes
  - ALL_CAPS for constants
- Data structures: Use Python dataclasses or Pydantic models for Task representation
- Error handling: Graceful error messages, no silent failures
- Input validation: Validate all user inputs before processing

Architecture Constraints:
- Storage: In-memory only (lists, dictionaries) - NO file I/O, NO databases in Phase I
- Interface: Command-line only - NO GUI, NO web interface
- Dependencies: Minimal external libraries (prefer standard library)
- Task ID generation: Sequential integers or UUID (decide in spec)
- State management: Single in-memory data structure (e.g., List[Task])

Required Features (Basic Level):
1. Add Task - Create new todo items with title (required) and description (optional)
2. Delete Task - Remove tasks from list by ID
3. Update Task - Modify existing task title and/or description
4. View Task List - Display all tasks with ID, title, status, and description
5. Mark as Complete - Toggle task completion status (complete ↔ incomplete)

Code Quality Standards:
- Functions: Single responsibility, max 20 lines per function
- Classes: Clear purpose, minimal public methods
- Documentation: Docstrings for all public functions/classes
- Comments: Only for complex logic, not obvious operations
- Testing approach: Manual testing for Phase I (automated tests in Phase II)

Success Criteria:
- All 5 Basic Level features working correctly
- Console app runs without errors on Python 3.13+
- Clear command menu displayed on startup
- User can perform all CRUD operations in single session
- Tasks persist in memory during app runtime (lost on exit - expected)
- Input validation prevents crashes from invalid data
- Task IDs are unique and stable during session
- Status indicators clearly show complete vs incomplete tasks
- Code follows PEP 8 and includes type hints
- Repository includes:
  - Working source code in /src
  - Constitution file
  - Complete specs in /specs folder
  - README.md with installation and usage instructions
  - CLAUDE.md with Claude Code workflow documentation

Technology Stack (Non-Negotiable):
 - Language: Python 3.13+
 - Package Manager: UV
 - Version Control: Git + GitHub (public repository)

Prohibited Practices:
 - Skipping specification phase and directly coding
 - Using databases or file storage in Phase I
 - Adding features beyond Basic Level
 - Submitting incomplete or non-functional deliverables

Documentation Requirements:
  - README.md must include:
  - Project overview
  - Installation steps (UV setup, dependencies)
  - Usage instructions with examples
  - Feature list
  - Tech stack
- CLAUDE.md must include:
  - Spec-driven workflow explanation
  - Example prompts used
  - Iteration history (if specs were refined)
- Specs folder must include:
  - All specification versions
  - Feature specifications for each of 5 features
  - Architecture decisions
  - Data model specifications

This constitution governs Phase I only. Principles may evolve in Phase II when transitioning to web application with persistent storage.

## Response snapshot

I've updated the project constitution to match the requirements for the Todo In-Memory Python Console App. The new constitution includes:

- Core principles focused on Spec-Driven Development, Simplicity First, Clean Architecture, User-Centric Design, and Iterative Refinement
- Technology requirements specifying Python 3.13+, UV package manager, and PEP 8 compliance
- Architecture constraints for Phase I including in-memory storage only and command-line interface
- The 5 required basic features (Add, Delete, Update, View, Mark Complete)
- Code quality standards with function length limits and documentation requirements
- Success criteria for completing the Phase I deliverables
- Technology stack requirements (Python 3.13+, UV, Git/GitHub)
- Prohibited practices to ensure adherence to Phase I constraints
- Documentation requirements for README.md, CLAUDE.md, and specs folder

The constitution is now properly configured for the hackathon project focused on building a Python CLI todo application.

## Outcome

- ✅ Impact: Constitution completely updated from agent-focused to Python CLI app focused
- 🧪 Tests: none
- 📁 Files: Updated .specify/memory/constitution.md with new requirements
- 🔁 Next prompts: Ready to create specifications for the 5 basic features
- 🧠 Reflection: The constitution now properly guides development for the Python CLI todo app with clear constraints and requirements

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin creating feature specifications based on the new constitution