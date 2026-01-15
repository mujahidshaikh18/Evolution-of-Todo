# Backend Development Guide (FastAPI + SQLModel + Neon PostgreSQL)

## Core Principles
- Use FastAPI with Pydantic models for API development
- Leverage SQLModel for database modeling
- Follow RESTful API design principles
- Ensure proper authentication and security
- Maintain data integrity and validation

## Project Structure
```
backend/
├── main.py                 # Main application entry point
├── config.py              # Configuration settings
├── db.py                  # Database connection and session management
├── models.py              # SQLModel database models
├── schemas.py             # Pydantic schemas for request/response validation
├── middleware/
│   └── auth.py           # Authentication middleware
└── routes/
    └── tasks.py          # API route handlers
```

## API Design Standards
- Use RESTful endpoints: GET /items, POST /items, PUT /items/{id}, DELETE /items/{id}
- Implement proper HTTP status codes
- Use Pydantic models for request/response validation
- Include comprehensive API documentation
- Handle errors gracefully with proper status codes

## Database Best Practices
- Define models using SQLModel (SQLAlchemy + Pydantic)
- Use proper relationships between models
- Implement efficient queries with proper indexing
- Handle database sessions properly
- Use transactions for data consistency

## Authentication & Security
- Implement JWT-based authentication
- Secure API endpoints with proper validation
- Hash passwords using bcrypt
- Validate and sanitize all inputs
- Implement rate limiting where appropriate

## Error Handling
- Use HTTPException for returning error responses
- Implement custom exception handlers
- Log errors appropriately
- Return meaningful error messages
- Don't expose sensitive information in error responses

## Environment Configuration
- Use environment variables for configuration
- Store sensitive data in environment variables
- Implement proper CORS settings
- Configure database connection pooling
- Set up logging levels

## Testing Approach
- Write unit tests for individual functions
- Create integration tests for API endpoints
- Test database operations
- Validate authentication flow
- Test error scenarios

## Deployment Best Practices
- Use environment-specific configurations
- Implement health check endpoints
- Monitor API performance
- Set up proper logging
- Ensure proper SSL/TLS configuration