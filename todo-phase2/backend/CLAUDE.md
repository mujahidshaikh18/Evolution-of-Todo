# Claude Code Workflow for Todo Full-Stack Web Application - Backend

This document describes the Claude Code workflow for the backend of the Todo Full-Stack Web Application - Phase II.

## Backend Overview

The backend is built with FastAPI and uses SQLModel ORM to interact with a Neon Serverless PostgreSQL database. It provides a RESTful JSON API with JWT-based authentication and user isolation.

## Tech Stack
- **Framework**: FastAPI 0.104+
- **Language**: Python 3.11+
- **ORM**: SQLModel 0.0.16+
- **Database**: Neon Serverless PostgreSQL
- **Authentication**: Better Auth with JWT tokens
- **API Style**: RESTful JSON

## Key Components

1. **Main Application**: FastAPI app with CORS middleware and JWT authentication
2. **Models**: SQLModel entities for User and Task
3. **Schemas**: Pydantic models for request/response validation
4. **Middleware**: JWT verification and user isolation
5. **Routes**: Task management endpoints with user validation

## Directory Structure

```
backend/
├── CLAUDE.md
├── main.py
├── config.py
├── db.py
├── models.py
├── schemas.py
├── middleware/
│   └── auth.py
└── routes/
    └── tasks.py
```

## API Endpoints

- `GET /api/{user_id}/tasks` - Get all tasks for user
- `POST /api/{user_id}/tasks` - Create new task
- `GET /api/{user_id}/tasks/{id}` - Get specific task
- `PUT /api/{user_id}/tasks/{id}` - Update task
- `DELETE /api/{user_id}/tasks/{id}` - Delete task
- `PATCH /api/{user_id}/tasks/{id}/complete` - Toggle completion

All endpoints require JWT authentication via Authorization header.

## Security

- JWT-based authentication with Better Auth
- User isolation through user_id validation
- Input validation with Pydantic models
- SQL injection prevention via SQLModel/SQLAlchemy

## Usage

To run the backend development server:

```bash
pip install fastapi uvicorn sqlmodel python-jose[cryptography] passlib[bcrypt] python-multipart python-dotenv
uvicorn main:app --reload --port 8000
```

The API will be available at http://localhost:8000.