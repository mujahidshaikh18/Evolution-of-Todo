# Phase 3: AI-Powered Todo Chatbot with MCP Server

This phase implements an AI-powered chatbot interface for the todo application using Cohere AI and MCP (Model Context Protocol) server architecture.

## Features

### AI Integration
- Cohere's command-r-plus model accessed through OpenAI-compatible SDK
- Stateless chat architecture with database persistence
- Context-aware conversations with history management

### MCP Tools
- `manage_todo_mcp`: Full CRUD operations for todo items via natural language
- `sync_chat_memory`: Automated saving and retrieval of conversation history
- `proactive_guard`: Duplicate detection and deadline conflict checking
- `chat_handshake_mcp`: Initialize conversation context with recent history

### Architecture
- Stateless backend with database-backed conversation history
- MCP server running independently for AI tool exposure
- Cyberpunk-themed chat interface with smooth animations

## Setup

1. Install dependencies:
```bash
cd todo-phase2/backend
pip install -r requirements.txt
```

2. Configure environment variables:
```bash
cp .env.example .env
# Add your Cohere API key to .env
```

3. Run database migrations:
```bash
cd todo-phase2/backend
python -c "from db import create_db_and_tables; create_db_and_tables()"
```

4. Start the backend:
```bash
cd todo-phase2/backend
uvicorn main:app --reload
```

5. Start the MCP server:
```bash
cd phase3_ai_engine
python main.py
```

6. Start the frontend:
```bash
cd todo-phase2/frontend
npm run dev
```

## Usage

1. Access the application at http://localhost:3000
2. Use the chat interface to manage your tasks with natural language
3. Examples:
   - "Add a task to buy groceries"
   - "Mark task #1 as completed"
   - "Update the description of task #2"
   - "Delete task #3"

## Project Structure

```
├── phase3_ai_engine/           # MCP server and AI components
│   ├── ai_client.py          # Cohere API integration
│   ├── mcp_server.py         # MCP server foundation
│   ├── services/
│   │   ├── chat_service.py   # Chat history management
│   │   ├── session_service.py # Session management
│   │   └── validation_service.py # Validation utilities
│   └── mcp_tools/            # MCP tool implementations
│       ├── todo_tool.py      # manage_todo_mcp
│       ├── chat_memory_tool.py # sync_chat_memory
│       ├── proactive_guard_tool.py # proactive_guard
│       └── handshake_tool.py # chat_handshake_mcp
├── todo-phase2/
│   ├── backend/
│   │   ├── routes/
│   │   │   └── chat.py      # Chat API endpoints
│   │   ├── models.py        # ChatHistory model
│   │   └── services/
│   │       └── validation_service.py # Task validation
│   └── frontend/
│       ├── components/
│       │   ├── ChatInterface.tsx # Chat UI component
│       │   └── ChatContainer.tsx # Chat modal container
│       ├── lib/
│       │   └── api-client.ts # Updated with chat methods
│       └── hooks/
│           └── useChat.ts    # Chat hook
│   └── app/
│       └── dashboard/
│           └── page.tsx     # Dashboard with chat integration
```

## Technologies Used

- **Backend**: FastAPI, SQLModel, PostgreSQL
- **AI**: Cohere command-r-plus via OpenAI-compatible SDK
- **MCP**: Model Context Protocol for AI tool exposure
- **Frontend**: React, TypeScript, Tailwind CSS, Framer Motion
- **Database**: Neon PostgreSQL with chat history table

## Architecture Decisions

### ADR-006: AI Integration with Cohere via OpenAI-Compatible SDK
Using Cohere's command-r-plus model accessed through the OpenAI-compatible SDK interface balances the requirement to use Cohere with familiarity of OpenAI SDK patterns.

### ADR-007: MCP Server Architecture for AI Tools
Creating a separate MCP server application in the `phase3_ai_engine` directory provides clear separation between AI tools and main backend functionality.

### ADR-008: Stateless Chat Architecture with Database Persistence
Implementing a stateless architecture where all chat history is stored in the database enables the "stateless handshake" pattern while maintaining horizontal scaling capabilities.