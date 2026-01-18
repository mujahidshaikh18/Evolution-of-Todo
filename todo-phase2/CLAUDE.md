# Claude Code Workflow for Todo Full-Stack Web Application - Phase II

This document describes the Claude Code workflow used to develop the Todo Full-Stack Web Application - Phase II.

## Project Overview

The Todo Full-Stack Web Application is a modern web application with Next.js frontend and FastAPI backend that transforms the Phase I console app into a web application with persistent database storage, user authentication via Better Auth with JWT tokens, and responsive UI accessible from any browser. The application implements all 5 Basic Level features (Add, View, Update, Complete, Delete tasks) with proper user isolation ensuring each user only sees their own tasks.

## Development Process

### Tech Stack
- **Frontend**: Next.js 16+ (App Router), TypeScript, Tailwind CSS
- **Backend**: Python FastAPI, SQLModel ORM
- **Database**: Neon Serverless PostgreSQL
- **Authentication**: Better Auth with JWT tokens
- **API Style**: RESTful JSON
- **Deployment**: Vercel (frontend), Backend hosted separately

### Architecture
- Monorepo structure (frontend + backend)
- RESTful API with user isolation (JWT-based)
- Stateless backend
- Database as single source of truth

## Key Features Implemented

1. **User Registration & Authentication**: Create accounts with email/password, JWT token management
2. **Create Tasks**: Add new tasks with required title and optional description
3. **View Tasks**: Display all user's tasks with ID, title, status ([x]/[ ]), and description
4. **Update Tasks**: Modify existing task title or description
5. **Complete Tasks**: Toggle task completion status (complete ↔ incomplete)
6. **Delete Tasks**: Remove tasks by ID with confirmation
7. **User Isolation**: Each user sees only their own tasks, secured by JWT validation

## Directory Structure

```
todo-phase2/
├── CLAUDE.md
├── README.md
├── frontend/
│   ├── CLAUDE.md
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   ├── dashboard/
│   │   │   └── page.tsx
│   │   └── auth/
│   │       ├── signin/
│   │       │   └── page.tsx
│   │       └── signup/
│   │           └── page.tsx
│   ├── components/
│   │   ├── TaskList.tsx
│   │   ├── TaskCard.tsx
│   │   ├── AddTaskModal.tsx
│   │   ├── EditTaskModal.tsx
│   │   └── Navbar.tsx
│   ├── lib/
│   │   ├── auth.ts
│   │   ├── api-client.ts
│   │   └── types.ts
│   ├── package.json
│   └── tailwind.config.ts
├── backend/
│   ├── CLAUDE.md
│   ├── main.py
│   ├── config.py
│   ├── db.py
│   ├── models.py
│   ├── schemas.py
│   ├── middleware/
│   │   └── auth.py
│   └── routes/
│       └── tasks.py
├── docker-compose.yml
└── .env.example
```

## Usage

To run the application:

### Backend
```bash
cd backend
pip install fastapi uvicorn sqlmodel python-jose[cryptography] passlib[bcrypt] python-multipart python-dotenv
uvicorn main:app --reload --port 8000
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

The frontend will be available at http://localhost:3000 and the backend API at http://localhost:8000.