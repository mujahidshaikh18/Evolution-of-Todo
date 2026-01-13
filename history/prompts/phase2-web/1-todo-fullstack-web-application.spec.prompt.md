---
id: spec-001
stage: spec
feature: phase2-web
title: Todo Full-Stack Web Application - Phase II
created: 2026-01-09
author: Claude Sonnet 4.5
tags: [web, fullstack, authentication, todo, phase2]
status: completed
---

# Prompt History Record: Todo Full-Stack Web Application - Phase II

## Original Prompt

```
Todo Full-Stack Web Application - Phase II

Target audience: Hackathon participants building production-ready multi-user web apps with Spec-Driven Development

Focus: Transform Phase I console app into modern web application with persistent database storage, user authentication, and responsive UI accessible from any browser

User Journeys:

Journey 1: New User Registration & First Task
- User visits web app landing page
- Clicks "Sign Up" button
- Enters email, password, and name
- Better Auth creates account and logs in automatically
- User redirected to dashboard showing empty task list
- User clicks "Add Task" button
- Enters task title and description in modal/form
- Submits → task appears in list immediately
- Task persists across browser sessions

Journey 2: Returning User Login & Task Management
- User visits web app
- Clicks "Sign In" button
- Enters credentials → Better Auth validates
- JWT token issued and stored
- User sees their task list (only their tasks)
- User can add, edit, delete, complete tasks via UI
- All changes reflected in real-time
- User logs out → data persists in database

Journey 3: Creating and Viewing Tasks (Web UI)
- Authenticated user on dashboard
- Clicks "New Task" button → modal opens
- Enters title (required), description (optional)
- Submits → API call with JWT token
- Backend validates token, extracts user_id
- Task saved to database with user_id association
- Frontend updates task list without page reload
- User sees task with status indicator

Journey 4: Updating Tasks (Web UI)
- User clicks "Edit" icon on task card
- Modal opens with current task data pre-filled
- User modifies title and/or description
- Submits → API call with JWT token
- Backend validates ownership (user_id matches)
- Task updated in database
- Frontend refreshes task display
- User sees updated information

Journey 5: Completing and Deleting Tasks (Web UI)
- User clicks checkbox/toggle on task → status changes to complete
- API call with JWT token → backend updates database
- Visual indicator changes (strikethrough, checkmark, color)
- User clicks "Delete" icon → confirmation prompt
- Confirms → API call with JWT token
- Backend validates ownership and deletes
- Task removed from UI
- Database updated immediately

Journey 6: User Isolation & Security
- User A logs in → sees only their 10 tasks
- User B logs in simultaneously → sees only their 5 tasks
- User A cannot access User B's tasks via API
- All API requests require valid JWT token
- Invalid/expired tokens return 401 Unauthorized
- Users cannot modify/view others' data

Success Criteria:

Authentication & Security:
- User can sign up with email/password
- User can sign in and receive JWT token
- JWT token included in all API requests (Authorization header)
- Backend validates JWT and extracts user_id
- All database queries filtered by user_id
- Invalid tokens rejected with 401 status
- Users completely isolated (cannot see others' data)

Feature Completeness:
- All 5 Basic Level features working as web app
- Responsive UI works on desktop and mobile
- Real-time updates without page refresh
- Data persists in Neon PostgreSQL database
- Frontend deployed to Vercel
- Backend accessible via public URL
- No console/CLI interface needed

User Experience:
- Clean, modern UI with Tailwind CSS
- Loading states while API calls process
- Success/error messages for user actions
- Intuitive navigation and task management
- Form validation before submission
- Mobile-responsive layout

Technical Quality:
- Monorepo structure with /frontend and /backend
- Next.js App Router patterns (server/client components)
- RESTful API endpoints following convention
- SQLModel ORM for type-safe database operations
- Environment variables for secrets (not hardcoded)
- CORS configured correctly
- Error handling on frontend and backend

Spec-Driven Evidence:
- Spec-Kit Plus configuration in /.spec-kit/
- Organized specs in /specs folder (features, api, database, ui)
- CLAUDE.md files at root, /frontend, /backend
- All code generated via Claude Code (documented)
- README with setup instructions for both frontend and backend

Acceptance Criteria:

Authentication (Better Auth + JWT):
- GIVEN new user visits app
- WHEN clicks "Sign Up" and enters valid email/password
- THEN account created, JWT token issued, redirected to dashboard
- VERIFY token stored in client, subsequent API calls include token

- GIVEN existing user
- WHEN enters correct credentials
- THEN JWT token issued, user sees their task list
- WHEN enters incorrect credentials
- THEN error message displayed, no token issued

- GIVEN authenticated user
- WHEN JWT token expires (after 7 days)
- THEN API returns 401, user redirected to login

Add Task (Web):
- GIVEN authenticated user on dashboard
- WHEN clicks "Add Task" button
- THEN modal/form appears with title and description fields
- WHEN submits with valid title (1-200 chars)
- THEN POST /api/{user_id}/tasks with JWT token
- AND backend creates task associated with user_id
- AND frontend updates list without reload
- VERIFY task persists in database
- WHEN submits empty title
- THEN validation error shown, task not created

List Tasks (Web):
- GIVEN authenticated user with 5 tasks (3 incomplete, 2 complete)
- WHEN dashboard loads
- THEN GET /api/{user_id}/tasks with JWT token
- AND displays all 5 tasks with ID, title, status, description
- AND complete tasks have visual indicator (checkmark, strikethrough)
- VERIFY only current user's tasks shown
- WHEN user has no tasks
- THEN empty state message "No tasks yet. Create your first one!"

Update Task (Web):
- GIVEN authenticated user viewing task list
- WHEN clicks "Edit" on task ID 3
- THEN modal opens with current title/description pre-filled
- WHEN modifies title to "Updated Task"
- THEN PUT /api/{user_id}/tasks/3 with JWT token
- AND backend validates user owns task
- AND database updated
- AND frontend shows updated title
- VERIFY changes persist on page reload
- WHEN user tries to edit another user's task (direct API call)
- THEN 403 Forbidden returned

Delete Task (Web):
- GIVEN authenticated user viewing task list
- WHEN clicks "Delete" icon on task ID 2
- THEN confirmation prompt appears
- WHEN confirms deletion
- THEN DELETE /api/{user_id}/tasks/2 with JWT token
- AND backend validates ownership
- AND task removed from database
- AND frontend removes task from UI
- VERIFY task no longer appears on reload

Complete Task (Web):
- GIVEN authenticated user viewing incomplete task ID 4
- WHEN clicks checkbox/toggle
- THEN PATCH /api/{user_id}/tasks/4/complete with JWT token
- AND backend toggles completed field to true
- AND frontend shows visual change (checkmark, strikethrough, color)
- WHEN clicks again
- THEN toggles back to incomplete
- VERIFY status persists in database

API Endpoints:

Required REST API:
- GET /api/{user_id}/tasks - List all user's tasks
- POST /api/{user_id}/tasks - Create new task
- GET /api/{user_id}/tasks/{id} - Get task details
- PUT /api/{user_id}/tasks/{id} - Update task
- DELETE /api/{user_id}/tasks/{id} - Delete task
- PATCH /api/{user_id}/tasks/{id}/complete - Toggle completion

All endpoints:
- Require JWT token in Authorization: Bearer <token> header
- Validate token and extract user_id
- Filter/validate data by user_id
- Return JSON responses
- Handle errors with appropriate status codes

Database Schema:

users table (managed by Better Auth):
- id: string (primary key)
- email: string (unique, not null)
- name: string
- created_at: timestamp
- (Better Auth manages password hashing, sessions)

tasks table:
- id: serial primary key (auto-increment integer)
- user_id: string (foreign key → users.id, not null)
- title: string (not null, max 200 chars)
- description: text (nullable, max 1000 chars)
- completed: boolean (default false)
- created_at: timestamp (default now())
- updated_at: timestamp (default now())

Indexes:
- tasks.user_id (for filtering by user)
- tasks.completed (for status filtering - optional)

Constraints:

Technical Stack (Non-Negotiable):
- Frontend: Next.js 16+ (App Router), TypeScript, Tailwind CSS
- Backend: Python FastAPI, SQLModel ORM
- Database: Neon Serverless PostgreSQL
- Authentication: Better Auth with JWT
- Deployment: Vercel (frontend), hosted backend (Railway/Render/etc)
- Spec Tools: Claude Code, Spec-Kit Plus, Monorepo structure

Development Process:
- MUST use monorepo structure with Spec-Kit Plus
- MUST implement feature-by-feature (backend + frontend together)
- MUST document Claude Code workflow in CLAUDE.md files
- MUST use Better Auth (not custom auth)

Monorepo Structure:
```
todo-phase2/
├── .spec-kit/
│   └── config.yaml
├── specs/
│   ├── constitution.md
│   ├── specify.md
│   ├── plan.md
│   ├── tasks.md
│   ├── features/
│   ├── api/
│   ├── database/
│   └── ui/
├── CLAUDE.md
├── README.md
├── frontend/
│   ├── CLAUDE.md
│   ├── app/
│   ├── components/
│   └── lib/
├── backend/
│   ├── CLAUDE.md
│   ├── main.py
│   ├── models.py
│   ├── routes/
│   └── db.py
└── docker-compose.yml
```

Security Requirements:
- JWT tokens shared secret (BETTER_AUTH_SECRET env var)
- Frontend attaches JWT to all API calls
- Backend validates JWT signature
- Backend extracts user_id from token
- Backend matches user_id in URL with token user_id
- All user data filtered by user_id in database queries
- No API endpoint returns data from other users
- Environment variables for secrets (never commit to Git)

Feature Scope (Phase II Only):
- Basic Level features as web app
- User authentication (signup/signin)
- Multi-user support with data isolation
- No AI chatbot (Phase III)
- No Kubernetes deployment (Phase IV)
- No advanced features like priorities, tags, reminders (Phase V)

Not Building (Deferred to Later Phases):

Phase III Features (Not in Phase II):
- AI chatbot interface
- Natural language commands
- MCP server
- OpenAI Agents SDK integration
- Conversational UI

Phase IV Features (Not in Phase II):
- Docker containerization
- Kubernetes deployment
- Minikube setup
```

## Response Summary

Created comprehensive specification document for the Todo Full-Stack Web Application - Phase II. The specification includes:

1. Six prioritized user stories covering:
   - User registration & authentication (P1)
   - Create and manage tasks (P1)
   - View personal task list (P1)
   - Update task details (P2)
   - Complete and delete tasks (P2)
   - Multi-user security & isolation (P1)

2. Detailed acceptance scenarios for each user story using Given/When/Then format

3. Comprehensive functional requirements (FR-001 to FR-015) covering authentication, task management, data persistence, and security

4. Key entities definition (User and Task)

5. Success criteria with measurable outcomes (SC-001 to SC-008)

6. Edge cases addressing security, validation, and error handling

The specification follows the Spec-Kit Plus methodology and is ready for the planning phase. A quality checklist was also created to validate the specification completeness.

## Status

Completed - Specification is ready for planning phase