# API Contract: Task Management API - Phase II

**Date**: 2026-01-09
**Feature**: Todo Full-Stack Web Application - Phase II
**Plan**: [Implementation Plan](../plan.md)

## Overview

RESTful JSON API for task management with user isolation. All endpoints require JWT authentication via Authorization header.

## Authentication

All endpoints (except health check) require JWT token in Authorization header:
```
Authorization: Bearer <jwt_token>
```

## Base URL
```
http://localhost:8000/api/{user_id}/
```

## Common Response Format

Success responses follow this pattern:
```json
{
  "id": integer,
  "user_id": string,
  "title": string,
  "description": string,
  "completed": boolean,
  "created_at": string (ISO 8601),
  "updated_at": string (ISO 8601)
}
```

Error responses follow this pattern:
```json
{
  "detail": "Error message"
}
```

## Endpoints

### GET /tasks
**Description**: Get all tasks for the authenticated user

**Headers**:
- Authorization: Bearer <token>

**Path Parameters**:
- user_id: string (must match JWT user_id)

**Query Parameters**: None

**Response Codes**:
- 200: Success - Returns array of tasks
- 401: Unauthorized - Invalid/missing JWT
- 403: Forbidden - user_id doesn't match JWT user_id

**Example Request**:
```
GET /api/12345/tasks
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Example Response (200)**:
```json
[
  {
    "id": 1,
    "user_id": "12345",
    "title": "Sample task",
    "description": "Sample description",
    "completed": false,
    "created_at": "2026-01-09T10:00:00Z",
    "updated_at": "2026-01-09T10:00:00Z"
  }
]
```

### POST /tasks
**Description**: Create a new task for the authenticated user

**Headers**:
- Authorization: Bearer <token>
- Content-Type: application/json

**Path Parameters**:
- user_id: string (must match JWT user_id)

**Request Body**:
```json
{
  "title": "Task title (required, 1-200 chars)",
  "description": "Task description (optional, max 1000 chars)"
}
```

**Response Codes**:
- 201: Created - Returns created task
- 400: Bad Request - Invalid input
- 401: Unauthorized - Invalid/missing JWT
- 403: Forbidden - user_id doesn't match JWT user_id

**Example Request**:
```
POST /api/12345/tasks
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

{
  "title": "New task",
  "description": "Task description"
}
```

**Example Response (201)**:
```json
{
  "id": 2,
  "user_id": "12345",
  "title": "New task",
  "description": "Task description",
  "completed": false,
  "created_at": "2026-01-09T10:00:00Z",
  "updated_at": "2026-01-09T10:00:00Z"
}
```

### GET /tasks/{id}
**Description**: Get a specific task by ID

**Headers**:
- Authorization: Bearer <token>

**Path Parameters**:
- user_id: string (must match JWT user_id)
- id: integer (task ID)

**Response Codes**:
- 200: Success - Returns task
- 401: Unauthorized - Invalid/missing JWT
- 403: Forbidden - user_id doesn't match JWT user_id or task doesn't belong to user
- 404: Not Found - Task doesn't exist

### PUT /tasks/{id}
**Description**: Update a specific task

**Headers**:
- Authorization: Bearer <token>
- Content-Type: application/json

**Path Parameters**:
- user_id: string (must match JWT user_id)
- id: integer (task ID)

**Request Body**:
```json
{
  "title": "Updated title (optional, 1-200 chars)",
  "description": "Updated description (optional, max 1000 chars)"
}
```

**Response Codes**:
- 200: Success - Returns updated task
- 400: Bad Request - Invalid input
- 401: Unauthorized - Invalid/missing JWT
- 403: Forbidden - user_id doesn't match JWT user_id or task doesn't belong to user
- 404: Not Found - Task doesn't exist

### DELETE /tasks/{id}
**Description**: Delete a specific task

**Headers**:
- Authorization: Bearer <token>

**Path Parameters**:
- user_id: string (must match JWT user_id)
- id: integer (task ID)

**Response Codes**:
- 200: Success - Returns {"message": "Task deleted"}
- 401: Unauthorized - Invalid/missing JWT
- 403: Forbidden - user_id doesn't match JWT user_id or task doesn't belong to user
- 404: Not Found - Task doesn't exist

**Example Response (200)**:
```json
{
  "message": "Task deleted"
}
```

### PATCH /tasks/{id}/complete
**Description**: Toggle task completion status

**Headers**:
- Authorization: Bearer <token>

**Path Parameters**:
- user_id: string (must match JWT user_id)
- id: integer (task ID)

**Response Codes**:
- 200: Success - Returns updated task with toggled completion status
- 401: Unauthorized - Invalid/missing JWT
- 403: Forbidden - user_id doesn't match JWT user_id or task doesn't belong to user
- 404: Not Found - Task doesn't exist

## Error Responses

### 400 Bad Request
```json
{
  "detail": "Validation error: title must be 1-200 characters"
}
```

### 401 Unauthorized
```json
{
  "detail": "Not authenticated"
}
```

### 403 Forbidden
```json
{
  "detail": "Access denied: cannot access other user's tasks"
}
```

### 404 Not Found
```json
{
  "detail": "Task not found"
}
```

## Validation Rules

- Title: 1-200 characters
- Description: 0-1000 characters
- user_id in URL must match user_id in JWT token
- Users can only access their own tasks
- Task IDs must be integers