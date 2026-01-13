---
id: plan-001
stage: plan
feature: phase2-web
title: Todo Full-Stack Web Application - Phase II
created: 2026-01-09
author: Claude Sonnet 4.5
tags: [web, fullstack, authentication, todo, phase2, planning]
status: completed
---

# Prompt History Record: Todo Full-Stack Web Application - Phase II

## Original Prompt

```
│   └── EditTaskModal.tsx
│   └── lib/
│   ├── auth.ts               # Better Auth config
│   ├── api-client.ts         # Backend API calls
│   └── types.ts
└── backend/
├── CLAUDE.md
├── main.py                   # FastAPI app
├── config.py                 # Env vars
├── db.py                     # Database connection
├── models.py                 # SQLModel Task
├── schemas.py                # Pydantic schemas
├── middleware/
│   └── auth.py               # JWT verification
└── routes/
└── tasks.py              # 6 REST endpoints
```

Backend Components (FastAPI):

main.py:
- FastAPI app + CORS middleware
- Include JWT middleware
- Include task routes
- Health endpoint: GET /health

models.py (SQLModel):
```python
Task:
- id: int (primary key, auto)
- user_id: str (foreign key, indexed)
- title: str (max 200)
- description: Optional[str] (max 1000)
- completed: bool (default False)
- created_at: datetime (auto)
- updated_at: datetime (auto)
```

middleware/auth.py:
- Extract JWT from Authorization: Bearer <token>
- Verify signature with BETTER_AUTH_SECRET
- Decode to get user_id (from "sub" claim)
- Inject user_id into request
- Return 401 if invalid

routes/tasks.py:
- GET /api/{user_id}/tasks
- POST /api/{user_id}/tasks
- GET /api/{user_id}/tasks/{id}
- PUT /api/{user_id}/tasks/{id}
- DELETE /api/{user_id}/tasks/{id}
- PATCH /api/{user_id}/tasks/{id}/complete
- All routes validate URL user_id matches JWT user_id

Frontend Components (Next.js):

app/dashboard/page.tsx:
- Protected route (redirect if not authenticated)
- Fetch tasks with JWT token
- Render TaskList component

components/TaskList.tsx:
- Map tasks to TaskCard components
- Show empty state if no tasks

components/TaskCard.tsx:
- Display task with status indicator
- Checkbox → toggle complete
- Edit button → open EditTaskModal
- Delete button → confirm and delete

components/AddTaskModal.tsx:
- Form: title (required), description (optional)
- Submit → POST to backend with JWT

lib/api-client.ts:
- getTasks(), createTask(), updateTask(), deleteTask(), toggleComplete()
- Attach JWT token from Better Auth session to all requests
- Handle 401 → redirect to login

lib/auth.ts:
- Better Auth configuration
- JWT plugin enabled
- Neon database adapter

Decisions Documented:

1. Monorepo: Single repo for easier Claude Code context
2. Task IDs: Auto-increment integers (database managed)
3. JWT Storage: Better Auth handles automatically
4. User Validation: Extract user_id from JWT, validate against URL
5. State Management: React useState (simple for Phase II)
6. Error Handling: Structured JSON responses with safe messages

Implementation Approach:

Setup Phase:
1. Initialize monorepo structure
2. Setup frontend (Next.js) and backend (FastAPI + SQLModel)
3. Configure Spec-Kit Plus
4. Setup Neon database connection
5. Configure Better Auth with JWT plugin

Authentication:
1. Better Auth signup/signin pages
2. JWT middleware in backend
3. Protected routes in frontend

Feature Implementation (Backend + Frontend Together):
1. Add Task: POST endpoint + modal form
2. List Tasks: GET endpoint + TaskList component
3. Update Task: PUT endpoint + edit modal
4. Complete Task: PATCH endpoint + checkbox
5. Delete Task: DELETE endpoint + delete button

Polish:
- Error handling and loading states
- Responsive design
- User isolation testing

API Contract:

All endpoints require: Authorization: Bearer <jwt_token>

GET /api/{user_id}/tasks
→ TaskResponse[]

POST /api/{user_id}/tasks
Body: {"title": "string", "description": "string?"}
→ TaskResponse (201)

PUT /api/{user_id}/tasks/{id}
Body: {"title": "string?", "description": "string?"}
→ TaskResponse (200)

PATCH /api/{user_id}/tasks/{id}/complete
→ TaskResponse (200)

DELETE /api/{user_id}/tasks/{id}
→ {"message": "Task deleted"} (200)

Errors: 400, 401, 403, 404 with {"detail": "message"}

Security Implementation:

JWT Flow:
1. Frontend gets JWT from Better Auth after login
2. Frontend attaches to all API calls in Authorization header
3. Backend middleware verifies JWT signature
4. Backend extracts user_id from token
5. Backend validates URL user_id matches token user_id
6. Backend filters all queries by user_id

User Isolation:
- All database queries: WHERE user_id = {jwt_user_id}
- Task ownership validation before update/delete
- 403 Forbidden if user tries to access others' tasks

Testing Strategy:

Manual Validation:
- Authentication: signup, signin, protected routes
- Add Task: create, validation errors
- List Tasks: view all, empty state
- Update Task: edit title/description
- Complete Task: toggle status
- Delete Task: remove with confirmation
- User Isolation: two users cannot see each other's tasks
- Error Handling: invalid token, network errors
- Responsive: desktop, tablet, mobile

Quality Checks:
- TypeScript strict mode enabled
- Python type hints on all functions
- No hardcoded secrets (use env vars)
- JWT token never logged
- CO
```

## Response Summary

Successfully completed the planning phase for the Todo Full-Stack Web Application - Phase II. The following artifacts were created:

1. **Implementation Plan** (plan.md): Detailed plan with technical context, constitution check, and project structure
2. **Research Document** (research.md): Technical decisions for authentication, database, frontend architecture, API design, state management, and styling
3. **Data Model** (data-model.md): Database schema, entity definitions, and API request/response models
4. **Quickstart Guide** (quickstart.md): Setup instructions, configuration, and development workflow
5. **API Contracts** (contracts/tasks-api.md): Complete REST API specification with endpoints, request/response formats, and validation rules
6. **Agent Context Update**: Updated CLAUDE.md with new technology stack information

The plan follows the Spec-Kit Plus methodology and Phase II requirements from the constitution, including:
- Next.js 16+ frontend with TypeScript and Tailwind CSS
- FastAPI backend with SQLModel ORM
- Neon Serverless PostgreSQL database
- Better Auth with JWT tokens for authentication
- Monorepo structure with clear separation of concerns
- User isolation and security requirements

All constitution checks passed, ensuring compliance with Phase II requirements.

## Status

Completed - Planning phase is ready for task breakdown phase