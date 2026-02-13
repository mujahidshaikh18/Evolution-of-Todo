# MCP Server Specification

## Feature Overview
Create an MCP (Model Context Protocol) server that integrates Cohere AI with stateless database functionality and intelligent tools for todo management and chat interactions.

## User Scenarios & Testing

### Scenario 1: AI-Powered Todo Management
**Actor**: End user
**Flow**: User interacts with chat interface to create, read, update, and delete todo items using natural language
**Test**: User can say "Add a task to buy groceries" and the system creates a todo item, displays it in the UI, and confirms completion

### Scenario 2: Stateful Conversation with Stateless Architecture
**Actor**: End user
**Flow**: User engages in multi-turn conversation where context is maintained through database lookups rather than server state
**Test**: User can reference previous conversation items even after connection interruptions

### Scenario 3: Intelligent Task Validation
**Actor**: End user
**Flow**: User attempts to create duplicate tasks or tasks with approaching deadlines, system proactively alerts
**Test**: System detects and warns about duplicate entries before they're created

## Functional Requirements

### FR-1: AI Engine Configuration
- **Requirement**: System must integrate Cohere's command-r-plus model using OpenAI-Compatible SDK
- **Details**: Configure base URL and API keys to point to Cohere's endpoint while maintaining OpenAI Agents SDK structure
- **Acceptance Criteria**:
  - AI responds appropriately when queried through the compatible SDK
  - Connection to Cohere endpoint is stable and authenticated
  - Response format matches OpenAI SDK expectations

### FR-2: Stateless Database Schema
- **Requirement**: System must maintain conversation history in a stateless manner
- **Details**:
  - Use existing Neon PostgreSQL database from Phase 2
  - Database table `chat_history` with columns: `id` (UUID), `session_id` (String), `role` (user/assistant), `content` (Text), `created_at` (Timestamp)
  - Before processing each request, fetch the last 10 messages from the table
- **Acceptance Criteria**:
  - New conversations can retrieve historical context
  - Maximum of 10 messages are retrieved for context
  - Session isolation is maintained between different users

### FR-3: MCP Tools Integration
- **Requirement**: System must expose multiple MCP tools for different functionalities
- **Details**:
  - `manage_todo_mcp`: Handles Create, Read, Update, Delete for tasks via Natural Language
  - `chat_memory_mcp`: Fetches and saves conversation history to the DB
  - `proactive_guard_mcp`: Checks for duplicate tasks and upcoming deadlines
  - `chat_handshake_mcp`: Performs a stateless handshake to sync the UI and initiate conversation context
- **Acceptance Criteria**:
  - Each tool is accessible via MCP protocol
  - Tools perform their designated functions reliably
  - Error handling is implemented for each tool

### FR-4: Multi-Agent Coordination
- **Requirement**: System must coordinate between different specialized agents
- **Details**:
  - Architect Agent oversees the stateless handshake and Cohere integration
  - MCP Expert Agent maps user intent to the specific Todo tools
- **Acceptance Criteria**:
  - Agents communicate effectively without conflicts
  - Handoff between agents is seamless
  - User intent is correctly interpreted and routed

### FR-5: UI Integration
- **Requirement**: System must maintain the Cyberpunk/Task.Matrix theme while integrating new functionality
- **Details**:
  - Preserve visual design from Phase 2
  - Integrate OpenAI ChatKit pointing to Cohere for streaming chat interface
  - Ensure Todo UI and Chatbot work in sync
- **Acceptance Criteria**:
  - UI maintains consistent visual theme
  - Chat interface streams responses smoothly
  - Todo items created via chat appear in UI and vice versa

## Success Criteria

### Quantitative Measures
- 95% of natural language todo commands are correctly interpreted and executed
- Chat response time remains under 3 seconds for 90% of queries
- System maintains conversation context with 99% accuracy across connection interruptions
- Duplicate task detection prevents 90% of redundant entries

### Qualitative Measures
- Users can seamlessly switch between chat and UI for todo management
- Conversation flow feels natural and contextually aware
- System provides helpful proactive suggestions without being intrusive
- Overall user satisfaction rating of 4+ stars for the integrated experience

## Key Entities

### Entity 1: ChatMessage
- **Attributes**: id (UUID), session_id (String), role (user/assistant), content (Text), created_at (Timestamp)
- **Relationships**: Belongs to a session, part of conversation history

### Entity 2: TodoItem
- **Attributes**: id (UUID), content (Text), status (pending/completed), created_at (Timestamp), updated_at (Timestamp)
- **Relationships**: Associated with user session, may be referenced in chat history

### Entity 3: Session
- **Attributes**: id (UUID), user_id (String), created_at (Timestamp), last_active (Timestamp)
- **Relationships**: Contains multiple ChatMessages, associated with TodoItems

## Constraints & Assumptions

### Constraints
- Must not copy Phase 2 files directly, but build upon existing codebase
- Cohere integration must use OpenAI-Compatible SDK format
- Database operations must be stateless (no server-side session state)
- UI must maintain existing Cyberpunk/Task.Matrix theme
- Use existing Neon PostgreSQL database from Phase 2
- Implement all four MCP tools: manage_todo_mcp, chat_memory_mcp, proactive_guard_mcp, and chat_handshake_mcp
- Maintain full bidirectional synchronization between chatbot and existing todo UI

## Clarifications

### Session 2026-02-03
- Q: Which database should be used for the MCP server? → A: Use the existing Neon PostgreSQL database from Phase 2
- Q: Which MCP tools should be implemented? → A: Implement all four MCP tools (manage_todo_mcp, chat_memory_mcp, proactive_guard_mcp, chat_handshake_mcp)
- Q: How should the theme be handled for the chat interface? → A: Extend and integrate with the existing Cyberpunk/Task.Matrix theme from Phase 2
- Q: Which AI model should be used for the integration? → A: Use Cohere's command-r-plus model as specified in the requirements
- Q: How should synchronization work between chatbot and UI? → A: Full bidirectional synchronization between chatbot and existing todo UI

### Assumptions
- Cohere's command-r-plus model supports OpenAI-compatible API calls
- Existing todo UI components can be extended to work with chat interface
- Database connection is available and reliable
- Network connectivity to Cohere endpoints remains stable