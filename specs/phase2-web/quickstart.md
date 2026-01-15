# Quickstart Guide: Todo Full-Stack Web Application - Phase II

**Date**: 2026-01-09
**Feature**: Todo Full-Stack Web Application - Phase II
**Plan**: [Implementation Plan](plan.md)

## Prerequisites

- Node.js 18+ for frontend development
- Python 3.11+ for backend development
- PostgreSQL-compatible database (Neon Serverless recommended)
- Better Auth account or self-hosted auth solution
- Git for version control

## Environment Setup

### 1. Clone and Initialize Repository
```bash
git clone <repository-url>
cd todo-phase2
```

### 2. Backend Setup
```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install fastapi sqlmodel python-jose[cryptography] passlib[bcrypt] python-multipart python-dotenv

# Set up environment variables
cp .env.example .env
# Edit .env with your database URL and auth secrets
```

### 3. Frontend Setup
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install
# or
yarn install
# or
pnpm install
```

## Configuration

### 1. Environment Variables
Create `.env` files in both frontend and backend with the following:

**Backend (.env)**:
```
DATABASE_URL="postgresql://username:password@localhost:5432/todoapp"
BETTER_AUTH_SECRET="your-secret-key-here"
NEON_DATABASE_URL="your-neon-database-url"
```

**Frontend (.env.local)**:
```
NEXT_PUBLIC_API_URL="http://localhost:8000"
NEXT_PUBLIC_BETTER_AUTH_URL="http://localhost:8000/auth"
```

### 2. Database Setup
```bash
# Run database migrations
cd backend
python -m alembic upgrade head
# or if using SQLModel directly
python -c "from db import create_db_and_tables; create_db_and_tables()"
```

## Running the Application

### 1. Start Backend Server
```bash
cd backend
uvicorn main:app --reload --port 8000
```

### 2. Start Frontend Development Server
```bash
cd frontend
npm run dev
# App will be available at http://localhost:3000
```

## API Endpoints

### Authentication (via Better Auth)
- `POST /api/auth/signup` - User registration
- `POST /api/auth/signin` - User login
- `GET /api/auth/me` - Get current user

### Task Management
- `GET /api/{user_id}/tasks` - Get all user tasks
- `POST /api/{user_id}/tasks` - Create new task
- `GET /api/{user_id}/tasks/{id}` - Get specific task
- `PUT /api/{user_id}/tasks/{id}` - Update task
- `DELETE /api/{user_id}/tasks/{id}` - Delete task
- `PATCH /api/{user_id}/tasks/{id}/complete` - Toggle task completion

## Development Workflow

### 1. Setting Up Development Environment
1. Install all dependencies as described above
2. Configure environment variables
3. Set up database connection
4. Verify both frontend and backend start successfully

### 2. Making Changes
1. For backend changes: modify files in `backend/` directory
2. For frontend changes: modify files in `frontend/` directory
3. Use appropriate type definitions and validation
4. Test changes by running both servers

### 3. Testing the Application
1. Register a new user via the signup form
2. Create, read, update, and delete tasks
3. Verify user isolation (other users can't see your tasks)
4. Test JWT token handling and expiration
5. Verify responsive design on different screen sizes

## Common Commands

```bash
# Backend development
cd backend
uvicorn main:app --reload  # Start backend with auto-reload

# Frontend development
cd frontend
npm run dev  # Start frontend development server

# Database operations
cd backend
python -c "from models import create_db_tables; create_db_tables()"  # Initialize database

# Running tests (when implemented)
cd backend
pytest  # Backend tests
cd frontend
npm run test  # Frontend tests
```