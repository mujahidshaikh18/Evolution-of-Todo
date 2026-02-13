# Phase 3: MCP Server - Implementation Plan

## Technical Context

### Architecture Overview
The MCP Server will implement a stateless architecture connecting Cohere AI services with a database-backed conversation history system. Building upon the existing codebase, this phase introduces an AI-powered chat interface that integrates with the existing todo functionality.

### Core Components
- **AI Integration Layer**: Cohere API client using OpenAI-Compatible SDK
- **Database Layer**: Neon PostgreSQL with chat_history table
- **MCP Server**: Exposes todo operations as MCP tools
- **Frontend Integration**: ChatKit UI integrated with existing Cyberpunk theme

### Known Unknowns
- Specific Cohere API rate limits and pricing structure (NEEDS CLARIFICATION)
- Optimal context window size for retrieving chat history (NEEDS CLARIFICATION)
- MCP server deployment strategy (NEEDS CLARIFICATION)

## Constitution Check

### Compliance Verification
- ✅ Spec-Driven Development: Following specification from spec.md
- ✅ Progressive Enhancement: Building on existing codebase
- ✅ Clean Architecture: Separating AI, database, and UI concerns
- ✅ Production Quality: Stateful chat interface with proper error handling
- ✅ Documentation First: Maintaining comprehensive documentation

### Tech Stack Alignment
- **Frontend**: React with ChatKit (aligns with Phase III requirements)
- **AI Framework**: OpenAI Agents SDK with Cohere compatibility (Phase III requirement)
- **MCP Server**: Official MCP SDK (Phase III requirement)
- **Database**: Neon PostgreSQL (continuing from existing codebase)
- **Theme**: Cyberpunk/Task.Matrix (continuing from existing codebase)

### Architecture Principles
- ✅ Stateless backend with DB persistence (Phase III requirement)
- ✅ Conversation history in database (Phase III requirement)
- ✅ User isolation maintained (continuing from existing codebase)

## Gates Evaluation

### Feasibility Assessment
- **Technical Feasibility**: ✅ All required technologies are available
- **Integration Feasibility**: ✅ Can build upon existing codebase
- **Performance Feasibility**: ✅ Stateless architecture supports scalability
- **Security Feasibility**: ✅ Following established security patterns

## Phase 0: Outline & Research

### Research Requirements

#### Decision: Cohere API Configuration
**Rationale**: Need to determine optimal configuration for Cohere's command-r-plus model using OpenAI-compatible SDK
**Alternatives considered**:
- Direct Cohere SDK vs OpenAI-compatible wrapper
- Different Cohere models (command-light vs command-r-plus)
- Alternative AI providers (OpenAI, Anthropic)

#### Decision: Database Context Window Size
**Rationale**: Need to determine optimal number of messages to retrieve for context (user specified 10, but 10-15 mentioned in requirements)
**Alternatives considered**:
- Fixed 10 messages (as in spec)
- Configurable 10-15 messages window
- Adaptive window based on token count

#### Decision: MCP Server Deployment
**Rationale**: Need to determine how MCP server will be deployed alongside existing backend
**Alternatives considered**:
- Separate service running on different port
- Integrated into existing backend
- Containerized deployment

## Phase 1: Design & Contracts

### Data Model

#### Entity: ChatMessage
- **id**: UUID (Primary Key, auto-generated)
- **session_id**: String (Foreign Key to session, indexed)
- **role**: String (Values: "user", "assistant", "system")
- **content**: Text (Conversation content, max 10000 characters)
- **created_at**: Timestamp (Creation time, indexed for ordering)

#### Entity: Session
- **id**: UUID (Primary Key, auto-generated)
- **user_id**: String (Foreign Key to user, from auth)
- **created_at**: Timestamp (Creation time)
- **last_active**: Timestamp (Last interaction)

#### Relationships
- Sessions have many ChatMessages (one-to-many)
- ChatMessages belong to a Session (many-to-one)

### API Contracts

#### MCP Tool: manage_todo_mcp
- **Function**: Handle CRUD operations for todo items
- **Parameters**:
  - operation: String ("create", "read", "update", "delete", "complete")
  - task_data: Object (contains task details for create/update)
  - task_id: String (for read/update/delete operations)
- **Returns**: Object with operation result and affected task data
- **Error Handling**: Returns error object with code and message

#### MCP Tool: sync_chat_memory
- **Function**: Save and retrieve chat history from database
- **Parameters**:
  - session_id: String (identifier for conversation session)
  - action: String ("save", "fetch", "truncate")
  - message_data: Object (for save operations)
  - limit: Integer (for fetch operations, default 10)
- **Returns**: Array of chat messages or operation confirmation
- **Error Handling**: Returns error object with code and message

#### MCP Tool: proactive_guard
- **Function**: Check for duplicate tasks and deadline conflicts
- **Parameters**:
  - operation: String ("check_duplicates", "check_deadlines", "validate")
  - task_data: Object (task details to validate)
  - user_id: String (to scope validation to user's tasks)
- **Returns**: Object with validation results and suggestions
- **Error Handling**: Returns error object with code and message

#### MCP Tool: chat_handshake_mcp
- **Function**: Initialize conversation context and retrieve history
- **Parameters**:
  - session_id: String (conversation identifier)
  - user_id: String (user identifier)
  - context_size: Integer (number of messages to retrieve, default 10)
- **Returns**: Array of recent chat messages and session context
- **Error Handling**: Returns error object with code and message

### Database Schema Migration

#### Chat History Table Creation
```sql
CREATE TABLE chat_history (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_chat_history_session_created ON chat_history(session_id, created_at);
CREATE INDEX idx_chat_history_session_role ON chat_history(session_id, role);
```

## MCP Server Structure

### Directory Structure
- MCP Server path: `/phase3_ai_engine/`
- Backend path: `/backend/`
- Frontend path: `/frontend/`

### File Organization
- **MCP Server Files**: `/phase3_ai_engine/` - Contains all AI and MCP server code
- **Backend Files**: `/backend/` - Contains FastAPI application and database logic
- **Frontend Files**: `/frontend/` - Contains Next.js application and UI components

## Quickstart Guide

### Prerequisites
- Python 3.13+ with UV package manager
- Node.js 18+ for frontend development
- Existing backend running
- Cohere API key with access to command-r-plus model

### Setup Instructions

1. **Environment Configuration**
   ```bash
   # Copy environment template
   cp .env.example .env

   # Add Cohere API key
   export COHERE_API_KEY="your-cohere-api-key"
   export COHERE_MODEL="command-r-plus"
   ```

2. **MCP Server Installation**
   ```bash
   # Install MCP SDK
   pip install model-context-protocol

   # Install Cohere Python SDK
   pip install cohere
   ```

3. **Database Migration**
   ```bash
   # Run migration to create chat_history table
   cd backend && python -m alembic upgrade head
   ```

4. **Start MCP Server**
   ```bash
   # Start the MCP server
   cd phase3_ai_engine && python main.py
   ```

### Running the Application
1. Start the backend: `cd backend && uvicorn main:app --reload`
2. Start the MCP server: `cd phase3_ai_engine && python main.py`
3. Start the frontend: `cd frontend && npm run dev`
4. Access the application at http://localhost:3000

### Testing the Integration
1. Open the chat interface in the Cyberpunk-themed UI
2. Verify that chat messages are stored in the database
3. Test todo creation via chat commands
4. Confirm that todos created via chat appear in the UI
5. Verify that UI-created todos are accessible via chat