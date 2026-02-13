# Evolution of Todo: From CLI to Full-Stack Web Application

This repository documents the complete evolution of a simple todo application from a command-line interface (CLI) to a full-stack web application, showcasing the journey of software development and architecture progression.

## Project Phases

### Phase I: Todo In-Memory Python Console App
- **Type**: Command-line application
- **Technology**: Python 3.13+, standard library only
- **Storage**: In-memory (lost on exit as designed)
- **Features**: Basic CRUD operations (Add, View, Update, Complete, Delete tasks)
- **Location**: `./phase1/`
- **Documentation**: `./phase1/README.md`

### Phase II: Todo Full-Stack Web Application
- **Type**: Modern web application with Next.js frontend and FastAPI backend
- **Technology**: Next.js 16+, FastAPI, TypeScript, Tailwind CSS, SQLModel
- **Storage**: Persistent with Neon Serverless PostgreSQL
- **Features**: All Phase I features plus user authentication, user isolation, responsive UI
- **Location**: `./todo-phase2/`
- **Documentation**: `./todo-phase2/README.md`

<<<<<<< HEAD
### Phase III: AI-Powered Todo Chatbot with MCP Server
- **Type**: AI-powered chatbot interface with MCP (Model Context Protocol) server
- **Technology**: Cohere AI (command-r-plus), MCP Protocol, FastAPI, Next.js
- **Storage**: Persistent with Neon PostgreSQL for chat history
- **Features**: Natural language task management, MCP tools, proactive validation, stateless architecture
- **Location**: `./phase3_ai_engine/` and `./specs/phase3/`
- **Documentation**: `./specs/phase3/README.md`

=======
>>>>>>> be27deab3d3f566b1231b8e6365d105beb813b09
## Repository Structure

```
Evolution-of-Todo/
├── README.md                    # This file - overall project documentation
├── CLAUDE.md                    # Claude Code workflow for the entire evolution
├── phase1/                      # Phase I: CLI Console Application
│   ├── README.md               # Phase I documentation
│   ├── CLAUDE.md               # Phase I workflow
│   ├── src/                    # Phase I source code
│   ├── tests/                  # Phase I tests
│   ├── specs/                  # Phase I specifications
│   ├── pyproject.toml          # Phase I project configuration
│   └── TESTING.md              # Phase I testing documentation
├── todo-phase2/                # Phase II: Full-Stack Web Application
│   ├── README.md               # Phase II documentation
│   ├── CLAUDE.md               # Phase II workflow
│   ├── frontend/               # Next.js frontend
│   ├── backend/                # FastAPI backend
│   ├── docker-compose.yml      # Docker configuration
│   └── .env.example           # Environment configuration example
├── specs/                      # Cross-phase specifications
│   ├── phase1/                 # Phase I specific specs
│   └── phase2-web/             # Phase II specific specs
├── history/                    # Development history and prompts
│   ├── adr/                    # Architecture Decision Records
│   └── prompts/                # Claude Code prompts history
<<<<<<< HEAD
├── phase3_ai_engine/           # Phase III: AI-Powered Chatbot with MCP
│   ├── main.py                 # Main MCP server entry point
│   ├── ai_client.py            # Cohere AI integration
│   ├── mcp_server.py           # MCP server foundation
│   ├── services/               # Backend services
│   │   ├── chat_service.py     # Chat history management
│   │   ├── session_service.py  # Session management
│   │   └── validation_service.py # Validation utilities
│   └── mcp_tools/              # MCP tool implementations
│       ├── todo_tool.py        # manage_todo_mcp
│       ├── chat_memory_tool.py # sync_chat_memory
│       ├── proactive_guard_tool.py # proactive_guard
│       └── handshake_tool.py   # chat_handshake_mcp
├── specs/                      # Cross-phase specifications
│   ├── phase1/                 # Phase I specific specs
│   ├── phase2-web/             # Phase II specific specs
│   └── phase3/                 # Phase III specific specs
=======
>>>>>>> be27deab3d3f566b1231b8e6365d105beb813b09
└── ...
```

## Development Approach

This project follows the **Spec-Kit Plus** methodology with specification-driven development:

1. **Specification-Driven**: Features planned before implementation
2. **Phase-Based Evolution**: Each phase builds upon the previous with clear goals
3. **Architecture Documentation**: All decisions recorded in ADRs
4. **Quality Assurance**: Comprehensive testing at each phase
<<<<<<< HEAD
5. **AI Integration**: Phase III incorporates Cohere AI with MCP protocol for natural language processing
6. **Stateless Architecture**: Phase III implements stateless design with database persistence
=======
>>>>>>> be27deab3d3f566b1231b8e6365d105beb813b09

## Learning Objectives

This evolution demonstrates:
- Migration from CLI to web-based interfaces
- Transition from in-memory to persistent storage
- Addition of user authentication and data isolation
- Scaling from single-user to multi-user systems
- Modern web development practices
- API design and security considerations
<<<<<<< HEAD
- AI integration with natural language processing
- MCP (Model Context Protocol) for AI tool exposure
- Stateless architecture with database persistence
- Proactive validation and duplicate detection
=======
>>>>>>> be27deab3d3f566b1231b8e6365d105beb813b09

## Getting Started

- For Phase I (CLI): See `./phase1/README.md`
- For Phase II (Web App): See `./todo-phase2/README.md`
<<<<<<< HEAD
- For Phase III (AI Chatbot): See `./specs/phase3/README.md` and `./phase3_ai_engine/README.md`
=======
>>>>>>> be27deab3d3f566b1231b8e6365d105beb813b09

## Technologies Used

### Phase I
- Python 3.13+
- Standard library only
- Command-line interface

### Phase II
- **Frontend**: Next.js 16+, TypeScript, Tailwind CSS
- **Backend**: FastAPI, Python 3.11+, SQLModel
- **Database**: Neon Serverless PostgreSQL
- **Authentication**: JWT tokens

<<<<<<< HEAD
### Phase III
- **AI Integration**: Cohere command-r-plus via OpenAI-compatible SDK
- **MCP Protocol**: Model Context Protocol for AI tool exposure
- **Backend**: FastAPI, SQLModel, PostgreSQL with stateless architecture
- **Frontend**: React, TypeScript, Tailwind CSS with Cyberpunk theme
- **Database**: Neon PostgreSQL for persistent chat history
- **Validation**: Proactive task validation and duplicate detection

=======
>>>>>>> be27deab3d3f566b1231b8e6365d105beb813b09
## Contributing

Each phase can be developed independently. Follow the documentation in each phase directory for setup and contribution guidelines.

## License

This project is part of the Todo App Evolution series from CLI to Cloud-Native AI System.