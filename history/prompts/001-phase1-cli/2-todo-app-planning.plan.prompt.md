---
id: 2
title: Todo App Planning
stage: plan
date: 2026-01-02
surface: agent
model: Claude Sonnet 4.5
feature: phase1-cli
branch: 001-phase1-cli
user: user
command: sp.plan
labels: [plan, python, cli, todo, architecture]
links:
  spec: specs/001-phase1-cli/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-phase1-cli/plan.md
  - specs/001-phase1-cli/research.md
  - specs/001-phase1-cli/data-model.md
  - specs/001-phase1-cli/quickstart.md
  - specs/001-phase1-cli/contracts/cli-commands.md
tests:
  - none
---

## Prompt

─────────────────────────────────┘

Project Structure:
```
todo-phase1/
├── src/
│   ├── __init__.py
│   ├── main.py              # Entry point, CLI menu loop
│   ├── task.py              # Task dataclass/model
│   ├── todo_manager.py      # Business logic (CRUD operations)
│   └── utils.py             # Input validation, formatters
├── specs/
│   ├── constitution.md
│   ├── specify.md
│   ├── plan.md
│   └── tasks.md
├── README.md
├── CLAUDE.md
└── pyproject.toml           # UV configuration
```

Component Responsibilities:

1. task.py:
   - Task dataclass with id, title, description, completed, created_at
   - Auto-generate UUID or sequential ID on creation
   - Validation methods for title/description length

2. todo_manager.py:
   - In-memory storage: List[Task]
   - Methods: add_task(), delete_task(), update_task(), list_tasks(), toggle_complete()
   - Returns success/error messages
   - Handles ID lookups and validation

3. main.py:
   - Display welcome message and command menu
   - Command loop: parse user input → call todo_manager → display result
   - Commands: add, list, view <id>, update <id>, complete <id>, delete <id>, help, exit
   - Error handling and user feedback

4. utils.py:
   - validate_title(title: str) → bool
   - validate_description(desc: str) → bool
   - format_task_list(tasks: List[Task]) → str
   - parse_command(input: str) → tuple[str, Optional[int]]

Decisions Needing Documentation:

1. Task ID Generation:
   Options:
   - Sequential integers (1, 2, 3...)
   - UUID strings
   Tradeoff: Integers easier for CLI users, UUIDs avoid collisions
   Decision: Use sequential integers, reset on each session

2. Data Storage:
   Options:
   - List[Task] (ordered, indexed)
   - Dict[id, Task] (fast lookups)
   Tradeoff: List preserves order, Dict faster for updates/deletes
   Decision: List[Task] for simplicity, linear search acceptable for Phase I

3. Task Model:
   Options:
   - Dataclass (Python 3.7+)
   - Pydantic BaseModel (validation built-in)
   Tradeoff: Dataclass lighter, Pydantic more robust
   Decision: Dataclass for minimal dependencies

4. Status Display:
   Options:
   - Text: "Complete" / "Incomplete"
   - Symbols: ✓ / ✗
   - Checkbox: [x] / [ ]
   Decision: ✓ / ✗ symbols for visual clarity

5. Command Parsing:
   Options:
   - Manual string splitting
   - argparse library
   - Click library
   Tradeoff: Manual = simple, libraries = robust
   Decision: Manual parsing (simple split) for Phase I

Testing Strategy:

Manual validation checks (automated testing in Phase II):

1. Add Task Tests:
   - Valid title only → creates task
   - Valid title + description → creates task
   - Empty title → error message
   - Title > 200 chars → error message
   - Description > 1000 chars → error message

2. Delete Task Tests:
   - Valid ID → removes task
   - Invalid ID → error message
   - Empty list → error message

3. Update Task Tests:
   - Valid ID + new title → updates
   - Valid ID + new description → updates
   - Invalid ID → error message
   - Empty new values → no change

4. List Tasks Tests:
   - Empty list → "No tasks found"
   - Multiple tasks → formatted list with IDs
   - Mix of complete/incomplete → correct symbols

5. Complete Task Tests:
   - Incomplete task → toggles to complete
   - Complete task → toggles to incomplete
   - Invalid ID → error message

Technical Details:

Implementation Approach:
- Use iterative development: Task model → Manager → CLI
- Follow spec-first: write specs before Claude Code generation
- Single-file iterations: complete one component before next
- Test manually after each component

Data Flow:
1. User enters command → main.py parses input
2. main.py validates command → calls todo_manager method
3. todo_manager performs operation on List[Task]
4. Returns result/error → main.py displays to user

Command Syntax:
- add → prompts for title, then description
- list → displays all tasks
- view <id> → shows full task details
- update <id> → prompts for new values
- complete <id> → toggles status
- delete <id> → removes task
- help → shows command menu
- exit → quits app

Error Handling:
- Wrap operations in try-except
- Return user-friendly error messages
- Never crash, always return to command prompt
- Validate inputs before processing

Type Hints:
- All function signatures include types
- Use typing module: List, Optional, Tuple
- Example: def add_task(title: str, description: Optional[str] = None) -> Task

Code Style:
- PEP 8 compliant (line length 88 chars - Black default)
- Docstrings for public functions: Google style
- Constants in CAPS: MAX_TITLE_LENGTH = 200
- No global variables except for storage list

Quality Validation:
- Run with python 3.13+
- Test all 5 features manually
- Verify error handling with invalid inputs
- Check code follows constitution standards
- Confirm specs folder documents Claude Code usage

## Response snapshot

I have successfully created the implementation plan for the Todo In-Memory Python Console App. The plan includes:

1. **Implementation Plan** (plan.md): Comprehensive plan with technical context, constitution check, and project structure
2. **Research** (research.md): Key decisions made for task ID generation, data storage, task model, status display, and command parsing
3. **Data Model** (data-model.md): Detailed specification of the Task entity and TaskList collection with validation rules
4. **Quickstart Guide** (quickstart.md): Setup instructions, project structure, commands, and development workflow
5. **Contracts** (contracts/cli-commands.md): CLI command interface specification with input/output contracts

The plan follows the constitution requirements:
- Python 3.13+ with minimal dependencies (standard library)
- In-memory storage only (no file/database storage)
- Console interface only (no GUI/web interface)
- Sequential integer IDs for user-friendly CLI interaction
- Clean architecture with separation of concerns
- PEP 8 compliance with type hints

The implementation approach is structured with:
- Task dataclass in src/task.py
- Business logic in src/todo_manager.py
- CLI interface in src/main.py
- Utilities in src/utils.py

All 5 required CRUD operations are covered (Add, View, Update, Complete, Delete) with proper validation, error handling, and user feedback.

## Outcome

- ✅ Impact: Complete implementation plan created for Python CLI todo app
- 🧪 Tests: Manual validation approach defined (automated in Phase II)
- 📁 Files: Created plan.md, research.md, data-model.md, quickstart.md, and contracts/
- 🔁 Next prompts: Ready to proceed with implementation using /sp.tasks
- 🧠 Reflection: Plan aligns with constitution and specification requirements

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin implementation with /sp.tasks