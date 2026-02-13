# Claude Code Workflow for Todo Full-Stack Web Application - Frontend

This document describes the Claude Code workflow for the frontend of the Todo Full-Stack Web Application - Phase II.

## Frontend Overview

The frontend is built with Next.js 16+ using the App Router, TypeScript, and Tailwind CSS. It provides a responsive UI accessible from any browser with user authentication via Better Auth and JWT tokens.

## Tech Stack
- **Framework**: Next.js 16+ (App Router)
- **Language**: TypeScript 5.3+
- **Styling**: Tailwind CSS
- **Authentication**: Better Auth
- **State Management**: React useState and Context

## Key Components

1. **Layout**: Root layout with navigation and authentication context
2. **Pages**: Landing page, dashboard, auth pages (signin/signup)
3. **Components**: TaskList, TaskCard, AddTaskModal, EditTaskModal, Navbar
4. **Libraries**: API client for backend communication, authentication handlers, type definitions

## Directory Structure

```
frontend/
├── CLAUDE.md
├── app/
│   ├── layout.tsx
│   ├── page.tsx
│   ├── dashboard/
│   │   └── page.tsx
│   └── auth/
│       ├── signin/
│       │   └── page.tsx
│       └── signup/
│           └── page.tsx
├── components/
│   ├── TaskList.tsx
│   ├── TaskCard.tsx
│   ├── AddTaskModal.tsx
│   ├── EditTaskModal.tsx
│   └── Navbar.tsx
├── lib/
│   ├── auth.ts
│   ├── api-client.ts
│   └── types.ts
├── package.json
└── tailwind.config.ts
```

## API Integration

The frontend communicates with the backend API using JWT tokens for authentication. All API calls include the Authorization header with the Bearer token obtained from Better Auth.

## Usage

To run the frontend development server:

```bash
npm install
npm run dev
```

The application will be available at http://localhost:3000.