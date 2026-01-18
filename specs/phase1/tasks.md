---
description: "Task list for Todo In-Memory Python Console App implementation"
---

# Tasks: Todo In-Memory Python Console App - Phase I

**Input**: Design documents from `/specs/001-phase1-cli/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Manual validation only (automated testing in Phase II as per constitution)

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure per implementation plan in src/
- [x] T002 Create src/__init__.py
- [x] T003 [P] Create src/task.py file for Task dataclass
- [x] T004 [P] Create src/todo_manager.py file for business logic
- [x] T005 [P] Create src/main.py file for CLI interface
- [x] T006 [P] Create src/utils.py file for utilities

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T007 Create Task dataclass in src/task.py with id, title, description, completed, created_at fields
- [x] T008 Add validation methods to Task class for title/description length validation
- [x] T009 Create TodoManager class in src/todo_manager.py with in-memory List[Task] storage
- [x] T010 [P] Add add_task method to TodoManager with validation and unique ID generation
- [x] T011 [P] Add list_tasks method to TodoManager for retrieving all tasks
- [x] T012 [P] Add validation utilities in src/utils.py for title and description length
- [x] T013 [P] Add formatting utilities in src/utils.py for task display

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new todo items to their list with required title and optional description, receiving confirmation with unique task ID

**Independent Test**: Can be fully tested by running the 'add' command with a title and description, verifying that a task is created with a unique ID and appears in the task list.

### Implementation for User Story 1

- [x] T014 Implement add_task method in src/todo_manager.py with validation and unique ID generation
- [x] T015 Add validation logic for title (1-200 chars) and description (max 1000 chars) in src/task.py
- [x] T016 Implement add command parsing in src/main.py
- [x] T017 Implement user input prompts for title and description in src/main.py
- [x] T018 Display confirmation with new task ID after successful addition
- [x] T019 Test manual validation: add task with valid title → creates task with unique ID

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Allow users to see all their tasks at once with ID, title, completion status, and description

**Independent Test**: Can be fully tested by adding tasks and then running the 'list' command to see all tasks displayed with proper formatting.

### Implementation for User Story 2

- [x] T020 Implement list_tasks method in src/todo_manager.py to return all tasks
- [x] T021 Create format_task_list function in src/utils.py to display tasks with ID, title, status (✓/✗), and description
- [x] T022 Implement list command parsing in src/main.py
- [x] T023 Handle empty task list case to display "No tasks found"
- [x] T024 Test manual validation: add multiple tasks then run list command → all tasks displayed with proper formatting

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Complete Tasks (Priority: P2)

**Goal**: Allow users to mark tasks as completed by toggling status between complete/incomplete

**Independent Test**: Can be fully tested by adding a task, marking it as complete, and verifying the status change is reflected in the task list.

### Implementation for User Story 3

- [x] T025 Add toggle_complete method to TodoManager in src/todo_manager.py
- [x] T026 Implement complete command parsing in src/main.py
- [x] T027 Add validation to check if task ID exists before toggling status
- [x] T028 Display confirmation of status change after toggling
- [x] T029 Test manual validation: incomplete task → complete command → status toggles to complete

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Update Task Details (Priority: P2)

**Goal**: Allow users to modify existing task title or description

**Independent Test**: Can be fully tested by updating a task's details and verifying the changes are reflected when viewing the task list.

### Implementation for User Story 4

- [x] T030 Add update_task method to TodoManager in src/todo_manager.py
- [x] T031 Implement update command parsing in src/main.py
- [x] T032 Add user prompts for new title/description in src/main.py
- [x] T033 Update only provided fields (title or description) while preserving others
- [x] T034 Test manual validation: update task with new title → task title updated in list

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Delete Tasks (Priority: P2)

**Goal**: Allow users to remove tasks by ID

**Independent Test**: Can be fully tested by deleting a task and verifying it no longer appears in the task list.

### Implementation for User Story 5

- [x] T035 Add delete_task method to TodoManager in src/todo_manager.py
- [x] T036 Implement delete command parsing in src/main.py
- [x] T037 Add validation to check if task ID exists before deletion
- [x] T038 Display confirmation after successful deletion
- [x] T039 Test manual validation: delete existing task → task removed from list

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T040 [P] Add command menu display on startup in src/main.py
- [x] T041 Add error handling for invalid task IDs across all operations
- [x] T042 [P] Add help command to show available commands in src/main.py
- [x] T043 [P] Add exit command to quit application in src/main.py
- [x] T044 Add comprehensive error messages for all validation failures
- [x] T045 Add type hints to all functions in all modules following PEP 8
- [x] T046 Run quickstart validation to ensure all 5 features work without errors

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all components for User Story 1 together:
Task: "Implement add_task method in src/todo_manager.py with validation and unique ID generation"
Task: "Add validation logic for title (1-200 chars) and description (max 1000 chars) in src/task.py"
Task: "Implement add command parsing in src/main.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify functionality manually after each task or logical group
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence