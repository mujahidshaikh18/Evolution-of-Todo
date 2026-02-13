---
id: "001"
title: "Database Migration"
stage: "plan"
date_iso: "2026-02-03"
surface: "agent"
model: "Sonnet 4.5"
feature: "phase3"
branch: "main"
user: "user"
command: "sp.plan update karo Environment: - Backend: FastAPI (Python) - Frontend: Next.js (TypeScript) - Database: Neon (PostgreSQL) - AI: Cohere (via OpenAI-compatible SDK) Tasks: 1. **Database Migration:** Add `chat_history` table to the existing Neon database using my current migration tool (Alembic/SQLAlchemy). 2. **FastAPI AI Integration:** Configure Cohere in the backend and create an endpoint that handles the 'Stateless Handshake'. 3. **MCP Server Logic:** Implement `manage_todo_mcp` and `chat_memory_mcp` within the FastAPI structure. 4. **Next.js UI:** Integrate the Chatbot overlay in the existing Cyberpunk UI. Start by Task 1: The Database Migration code for the `chat_history` table."
labels: ["database", "migration", "alembic", "postgresql"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - "todo-phase2/backend/models.py"
  - "todo-phase2/backend/alembic.ini"
  - "todo-phase2/backend/alembic/env.py"
  - "todo-phase2/backend/alembic/script.py.mako"
  - "todo-phase2/backend/alembic/versions/001_add_chat_history_table.py"
  - "todo-phase2/backend/db.py"
  - "todo-phase2/backend/requirements.txt"
  - "run_migration.py"
tests_yaml: []
---

# Database Migration Task Completion

## Summary
Successfully implemented the database migration for the `chat_history` table as requested for Phase 3 of the AI-Powered Todo Chatbot. The implementation includes:

1. Added the `ChatHistory` model to the existing models.py file with proper fields (id, session_id, role, content, created_at)
2. Created Alembic configuration files (alembic.ini, env.py, script.py.mako)
3. Created the migration script for the `chat_history` table with proper indexes
4. Updated the database configuration to include the new model in the metadata
5. Added Alembic to the requirements
6. Created a helper script to run the migration

## Technical Details

### ChatHistory Model
- **id**: UUID (Primary Key, auto-generated)
- **session_id**: String (Foreign Key to session, indexed)
- **role**: String (Values: "user", "assistant", "system")
- **content**: Text (Conversation content, max 10000 characters)
- **created_at**: Timestamp (Creation time, indexed for ordering)

### Indexes Created
- `idx_chathistory_session_created` on (session_id, created_at) for efficient chronological retrieval
- `idx_chathistory_session_role` on (session_id, role) for efficient role-based queries

## Files Modified/Created
- `todo-phase2/backend/models.py` - Added ChatHistory model
- `todo-phase2/backend/db.py` - Updated to include ChatHistory in metadata
- `todo-phase2/backend/requirements.txt` - Added alembic dependency
- `todo-phase2/backend/alembic.ini` - Alembic configuration
- `todo-phase2/backend/alembic/env.py` - Alembic environment setup
- `todo-phase2/backend/alembic/script.py.mako` - Alembic template
- `todo-phase2/backend/alembic/versions/001_add_chat_history_table.py` - Migration script
- `run_migration.py` - Helper script to execute migration

## Execution Instructions
To run the migration:
1. Install requirements: `pip install -r requirements.txt`
2. Run the migration: `python run_migration.py`

## Compliance Check
- ✅ Aligns with Phase 3 requirements for chat history persistence
- ✅ Uses existing tech stack (FastAPI, SQLModel, PostgreSQL)
- ✅ Implements proper database indexing for efficient retrieval
- ✅ Maintains compatibility with existing Phase 2 codebase
- ✅ Follows SQLAlchemy/Alembic best practices

## Next Steps
With the database migration complete, we can now proceed to Task 2: FastAPI AI Integration with Cohere and the 'Stateless Handshake' functionality.