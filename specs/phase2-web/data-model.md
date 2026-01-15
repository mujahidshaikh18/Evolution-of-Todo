# Data Model: Todo Full-Stack Web Application - Phase II

**Date**: 2026-01-09
**Feature**: Todo Full-Stack Web Application - Phase II
**Plan**: [Implementation Plan](plan.md)

## Database Schema

### Users Table (Managed by Better Auth)
```
users
├── id: string (primary key, unique)
├── email: string (unique, not null)
├── name: string (nullable)
├── created_at: timestamp
└── (Additional fields managed by Better Auth)
```

### Tasks Table
```
tasks
├── id: integer (primary key, auto-increment)
├── user_id: string (foreign key → users.id, indexed, not null)
├── title: string (not null, max 200 chars)
├── description: string (nullable, max 1000 chars)
├── completed: boolean (default false)
├── created_at: timestamp (default now())
└── updated_at: timestamp (default now())
```

**Indexes**:
- tasks.user_id (for filtering by user)
- tasks.completed (optional, for status filtering)

## Entity Definitions

### User Entity
- **Identity**: Email address (unique identifier)
- **Attributes**:
  - email: string (validation: proper email format)
  - name: string (optional, max 100 chars)
  - created_at: datetime (auto-generated)
- **Relationships**: One-to-many with Task entities
- **Validation**: Email must be unique and properly formatted

### Task Entity
- **Identity**: Auto-incrementing integer ID
- **Attributes**:
  - id: integer (auto-generated, primary key)
  - user_id: string (foreign key reference to User)
  - title: string (required, 1-200 characters)
  - description: string (optional, max 1000 characters)
  - completed: boolean (default false)
  - created_at: datetime (auto-generated)
  - updated_at: datetime (auto-generated)
- **Relationships**: Belongs to one User
- **Validation**:
  - Title must be 1-200 characters
  - Description must be ≤1000 characters if provided
  - user_id must reference an existing user

## API Request/Response Models

### Task Creation Request
```
{
  "title": string (required, 1-200 chars),
  "description": string? (optional, max 1000 chars)
}
```

### Task Response
```
{
  "id": integer,
  "user_id": string,
  "title": string,
  "description": string?,
  "completed": boolean,
  "created_at": string (ISO 8601 datetime),
  "updated_at": string (ISO 8601 datetime)
}
```

### Task Update Request
```
{
  "title": string? (optional, 1-200 chars),
  "description": string? (optional, max 1000 chars)
}
```

## State Transitions

### Task Completion
- **Initial State**: completed = false
- **Transition**: Toggle via PATCH /api/{user_id}/tasks/{id}/complete
- **Final State**: completed = true/false (toggled)

### Task Deletion
- **Initial State**: Task exists in database
- **Transition**: DELETE /api/{user_id}/tasks/{id}
- **Final State**: Task removed from database