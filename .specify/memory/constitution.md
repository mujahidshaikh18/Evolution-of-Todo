<!-- SYNC IMPACT REPORT
Version change: 1.2.0 → 1.3.0
Modified principles: Complete overhaul from agent-focused to Python CLI app focused
Added sections: Python-specific requirements, CLI architecture constraints, feature requirements
Removed sections: Agent-First Architecture, Multi-Platform Transformation Strategy (replaced with Python CLI focus)
Templates requiring updates:
- ⚠️ .specify/templates/plan-template.md - Needs Python CLI specific guidelines
- ⚠️ .specify/templates/spec-template.md - Needs CLI app specific structure
- ⚠️ .specify/templates/tasks-template.md - Needs Python CLI task types
Follow-up TODOs: Update templates to match new constitution
-->

# Todo In-Memory Python Console App Constitution

## Core Principles

### I. Spec-Driven Development
All development follows a strict specification-driven approach where requirements are captured in structured specifications before implementation. Every feature must have a corresponding specification document that defines WHAT needs to be built before determining HOW to build it.

### II. Simplicity First
Emphasize in-memory storage, console interface, and minimal dependencies. Solutions should be straightforward and avoid unnecessary complexity. Prefer standard library functions over external dependencies when possible.

### III. Clean Architecture
Maintain clear separation of concerns between data models, business logic, and user interface. Each component should have a single responsibility and be easily testable in isolation.

### IV. User-Centric Design
Create an intuitive command-line interface with clear feedback to users. The application should provide helpful error messages and guidance to ensure a positive user experience.

### V. Iterative Refinement
Refine specifications and implementations based on testing and feedback. Continuously improve the application through small, testable changes that build upon previous work.

## Key Standards

### Technology Requirements
- **Python version**: 3.13+ (strict requirement)
- **Package manager**: UV (required for dependency management)
- **Code style**: PEP 8 compliant, type hints mandatory for all functions and methods
- **Project structure**:
  - `/src` folder for all source code
  - `/specs` folder for all specification files
  - `README.md` with setup instructions
  - `CLAUDE.md` with Claude Code workflow instructions

### Naming Conventions
- `snake_case` for functions and variables
- `PascalCase` for classes
- `ALL_CAPS` for constants

### Data Structures
- Use Python dataclasses or Pydantic models for Task representation
- Implement proper type hints for all data structures
- Ensure data validation at the model level

### Error Handling
- Provide graceful error messages, no silent failures
- Handle all user input validation before processing
- Implement proper exception handling with user-friendly messages

## Architecture Constraints (Phase I - Hackathon II)

### Storage Requirements
- **Storage**: In-memory only (lists, dictionaries) - NO file I/O, NO databases in Phase I
- **State management**: Single in-memory data structure (e.g., List[Task])
- **Persistence**: Tasks persist in memory during app runtime but are lost on exit (expected behavior)

### Interface Requirements
- **Interface**: Command-line only - NO GUI, NO web interface
- **User experience**: Clear command menu displayed on startup
- **Navigation**: Intuitive command flow for all basic operations

### Dependencies
- **Dependencies**: Minimal external libraries (prefer standard library)
- **Task ID generation**: Sequential integers or UUID (to be decided in spec)
- **External integrations**: None in Phase I

## Required Features (Basic Level)

### 1. Add Task
Create new todo items with title (required) and description (optional). The system must validate input and assign unique IDs.

### 2. Delete Task
Remove tasks from list by ID. The system must validate that the task exists before deletion and handle invalid IDs gracefully.

### 3. Update Task
Modify existing task title and/or description. The system must validate that the task exists and apply changes appropriately.

### 4. View Task List
Display all tasks with ID, title, status, and description. The display must be clear and readable with proper formatting.

### 5. Mark as Complete
Toggle task completion status (complete ↔ incomplete). The system must validate the task exists and update the status appropriately.

## Code Quality Standards

### Function Requirements
- Functions: Single responsibility, maximum 20 lines per function
- Functions must have clear, descriptive names
- Functions must include type hints for all parameters and return values

### Class Requirements
- Classes: Clear purpose, minimal public methods
- Classes must follow the single responsibility principle
- Classes must include proper documentation

### Documentation Requirements
- Documentation: Docstrings for all public functions/classes
- Comments: Only for complex logic, not obvious operations
- All public APIs must be documented with examples where appropriate

### Testing Approach
- Testing: Manual testing for Phase I (automated tests in Phase II)
- All features must be manually verified before completion
- Edge cases must be tested with various input types

## Success Criteria

### Functional Requirements
- All 5 Basic Level features working correctly
- Console app runs without errors on Python 3.13+
- Clear command menu displayed on startup
- User can perform all CRUD operations in single session

### Quality Requirements
- Tasks persist in memory during app runtime (lost on exit - expected)
- Input validation prevents crashes from invalid data
- Task IDs are unique and stable during session
- Status indicators clearly show complete vs incomplete tasks

### Code Quality Requirements
- Code follows PEP 8 and includes type hints
- Repository includes working source code in /src
- Repository includes constitution file
- Repository includes complete specs in /specs folder
- Repository includes README.md with installation and usage instructions
- Repository includes CLAUDE.md with Claude Code workflow documentation

## Technology Stack (Non-Negotiable)

- **Language**: Python 3.13+
- **Package Manager**: UV
- **Version Control**: Git + GitHub (public repository)
- **Development Environment**: Local development with UV for dependency management

## Prohibited Practices

- Skipping specification phase and directly coding
- Using databases or file storage in Phase I
- Adding features beyond Basic Level
- Submitting incomplete or non-functional deliverables
- Hardcoding secrets or configuration values
- Violating PEP 8 style guidelines
- Skipping input validation

## Documentation Requirements

### README.md Requirements
- Project overview
- Installation steps (UV setup, dependencies)
- Usage instructions with examples
- Feature list
- Tech stack

### CLAUDE.md Requirements
- Spec-driven workflow explanation
- Example prompts used
- Iteration history (if specs were refined)

### Specs Folder Requirements
- All specification versions
- Feature specifications for each of 5 features
- Architecture decisions
- Data model specifications

## Governance

This constitution governs Phase I (Todo In-Memory Python Console App) only. Principles may evolve in Phase II when transitioning to web application with persistent storage. All code generated for this phase must comply with these requirements. Amendments to this constitution require documentation of impact on existing work and approval from project maintainers.

For development guidance, follow the established patterns in this constitution and ensure all implementation aligns with the specified technology stack and architecture constraints.

**Version**: 1.3.0 | **Ratified**: 2026-01-02 | **Last Amended**: 2026-01-02