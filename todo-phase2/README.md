# Todo Full-Stack Web Application - Phase II

A modern full-stack web application with Next.js frontend and FastAPI backend that transforms the Phase I console app into a web application with persistent database storage, user authentication, and responsive UI accessible from any browser.

## Features

- **User Authentication**: Secure registration and login with Better Auth and JWT tokens
- **Task Management**: Create, view, update, complete, and delete tasks
- **User Isolation**: Each user sees only their own tasks
- **Responsive Design**: Works on desktop and mobile devices
- **Persistent Storage**: Tasks stored in Neon Serverless PostgreSQL database

## Tech Stack

### Frontend
- Next.js 16+ (App Router)
- TypeScript 5.3+
- Tailwind CSS
- Better Auth for authentication

### Backend
- FastAPI 0.104+
- Python 3.11+
- SQLModel 0.0.16+
- Neon Serverless PostgreSQL

## Prerequisites

- Node.js 16+ for frontend
- Python 3.11+ for backend
- PostgreSQL-compatible database (Neon Serverless recommended)

## Setup

### Manual Setup

#### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install fastapi uvicorn sqlmodel python-jose[cryptography] passlib[bcrypt] python-multipart python-dotenv
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` with your database URL and auth secrets.

5. Run the backend server:
   ```bash
   uvicorn main:app --reload --port 8000
   ```

#### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env.local
   ```
   Edit `.env.local` with your backend API URL.

4. Run the frontend development server:
   ```bash
   npm run dev
   ```

### Docker Setup (Recommended)

1. Make sure you have Docker and Docker Compose installed.

2. Copy the environment variables:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` with your database URL and auth secrets.

3. Build and start the containers:
   ```bash
   docker-compose up --build
   ```

The application will be available at http://localhost:3000 with the backend API at http://localhost:8000.

## API Endpoints

All API endpoints follow the pattern: `http://localhost:8000/api/{user_id}/{endpoint}` and require JWT authentication via the `Authorization: Bearer <token>` header.

### Task Management
- `GET /api/{user_id}/tasks` - Get all tasks for user
- `POST /api/{user_id}/tasks` - Create new task
- `GET /api/{user_id}/tasks/{id}` - Get specific task
- `PUT /api/{user_id}/tasks/{id}` - Update task
- `DELETE /api/{user_id}/tasks/{id}` - Delete task
- `PATCH /api/{user_id}/tasks/{id}/complete` - Toggle completion status

## Environment Variables

### Backend (.env)
```
DATABASE_URL="postgresql://username:password@localhost:5432/todoapp"
BETTER_AUTH_SECRET="your-secret-key-here"
NEON_DATABASE_URL="your-neon-database-url"
```

### Frontend (.env.local)
```
NEXT_PUBLIC_API_URL="http://localhost:8000"
NEXT_PUBLIC_BETTER_AUTH_URL="http://localhost:8000/auth"
```

## Architecture

- **Monorepo structure**: Frontend and backend in a single repository
- **RESTful API**: JSON-based communication between frontend and backend
- **JWT Authentication**: Secure token-based authentication
- **User Isolation**: Each user's data is isolated using user_id validation

## Development

This project follows the Spec-Kit Plus methodology with specification-driven development. All features are planned before implementation according to the architecture decision records (ADRs).

## Testing

### Frontend Testing
1. Unit tests for React components using Jest and React Testing Library
2. Integration tests for API interactions
3. End-to-end tests using Playwright or Cypress

### Backend Testing
1. Unit tests for API endpoints using pytest
2. Database integration tests
3. Authentication and authorization tests
4. User isolation tests to ensure users can only access their own data

### Security Testing
1. Test that users cannot access other users' tasks
2. Validate JWT token expiration handling
3. Test input validation and sanitization
4. Test rate limiting and other security measures

To run tests:
- Backend: `pytest` (after installing dependencies with `pip install -r requirements.txt`)
- Frontend: `npm test` (after installing dependencies with `npm install`)

## Deployment

### Frontend
Deploy the Next.js application to Vercel, Netlify, or similar platforms:
1. Build the application: `npm run build`
2. Deploy the `out` directory

### Backend
Deploy the FastAPI application to cloud platforms like AWS, GCP, Azure, or Heroku:
1. Ensure environment variables are properly configured
2. Set up the production database
3. Configure SSL certificates for HTTPS

## Contributing

1. Follow the setup instructions above
2. Make changes according to the task breakdown in the specs directory
3. Test thoroughly to ensure user isolation and security requirements are met
4. Follow TypeScript and Python type hinting best practices

## License

This project is part of the Todo App Evolution series from CLI to Cloud-Native AI System.