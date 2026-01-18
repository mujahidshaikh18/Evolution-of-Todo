---
id: 1
title: Todo Console App Spec
stage: spec
date: 2026-01-02
surface: agent
model: Claude Sonnet 4.5
feature: phase1-cli
branch: 001-phase1-cli
user: user
command: sp.specify
labels: [spec, python, cli, todo, console]
links:
  spec: specs/001-phase1-cli/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-phase1-cli/spec.md
  - specs/001-phase1-cli/checklists/requirements.md
  - history/prompts/001-phase1-cli/1-todo-console-app-spec.spec.prompt.md
tests:
  - none
---

## Prompt

Todo In-Memory Python Console App - Phase I

Target audience: Hackathon participants using Spec-Driven Development with Claude Code

Focus: Command-line todo app with in-memory storage, demonstrating 5 Basic Level CRUD operations

User Journeys:

1. Create Task: User runs 'add' → enters title (required) and description (optional) → receives confirmation with task ID
2. View Tasks: User runs 'list' → sees all tasks with ID, title, status (✓/✗), and description
3. Update Task: User runs 'update <id>' → modifies title/description → sees confirmation
4. Complete Task: User runs 'complete <id>' → toggles status → sees status change in list
5. Delete Task: User runs 'delete <id>' → task removed → confirmed and no longer in list

Success Criteria:
- All 5 features work without errors
- Clear command menu on startup
- Graceful error handling for invalid inputs
- Task IDs remain stable during session
- Code follows PEP 8 with type hints
- Complete specs in /specs folder documenting Claude Code workflow

Acceptance Criteria:

Add Task:
- Title required (1-200 chars), description optional (max 1000 chars)
- Auto-generates unique ID, sets status to incomplete
- Displays confirmation with task ID

Delete Task:
- Removes task by ID, shows error if ID not found

Update Task:
- Prompts for new title/description, updates only provided fields
- Shows error if ID not found

View List:
- Displays: ID, Title, Status (✓ complete / ✗ incomplete), Description
- Shows "No tasks found" if empty

Mark Complete:
- Toggles status between complete/incomplete
- Shows confirmation of status change

Constraints:
- Python 3.13+, UV package manager
- In-memory storage only (list/dict, no database/files)
- Console interface only
- Standard library preferred
- Data lost on exit (expected)
- Spec-Driven Development

Data Model:
Task:
- id: int/str (unique, auto-generated)
- title: str (1-200 chars, required)
- description: str (max 1000 chars, optional)
- completed: bool (default False)
- created_at: datetime (auto-generate

## Response snapshot

I have successfully created a comprehensive specification for the Todo In-Memory Python Console App - Phase I. The specification includes:

1. Created feature directory: specs/001-phase1-cli/
2. Created specification file: specs/001-phase1-cli/spec.md
3. Created quality checklist: specs/001-phase1-cli/checklists/requirements.md
4. Created history directory: history/prompts/001-phase1-cli/

The specification contains:
- 5 prioritized user stories covering all 5 basic CRUD operations (Add, View, Update, Complete, Delete)
- Functional requirements (FR-001 through FR-010) covering all essential functionality
- Key entities (Task and TaskList)
- Success criteria (SC-001 through SC-007) with measurable outcomes
- Edge cases for error handling and boundary conditions
- Quality checklist validating all requirements

The specification follows the template structure and is ready for the planning phase. All requirements are testable and unambiguous, with clear acceptance scenarios for each user story. The specification is technology-agnostic in its success criteria while maintaining focus on the user value and business needs.

## Outcome

- ✅ Impact: Complete specification created for Python CLI todo app with 5 CRUD operations
- 🧪 Tests: none
- 📁 Files: Created spec.md, requirements.md checklist, and PHR file
- 🔁 Next prompts: Ready to proceed with /sp.plan for implementation planning
- 🧠 Reflection: Specification covers all required features with clear acceptance criteria

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin planning phase with /sp.plan