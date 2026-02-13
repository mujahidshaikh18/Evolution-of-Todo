# Phase 3 AI Engine

This directory contains the AI and MCP (Model Context Protocol) server components for the AI-Powered Todo Chatbot.

## Overview

The Phase 3 AI Engine implements:
- Cohere AI integration using OpenAI-compatible SDK
- MCP server for exposing tools to AI agents
- Chat service with database-backed conversation history
- MCP tools for todo management and validation

## Components

### AI Client
- `ai_client.py`: Cohere API client using OpenAI-compatible SDK
- Configured to use Cohere's command-r-plus model
- Handles authentication and API communication

### Chat Service
- `services/chat_service.py`: Manages conversation history and AI interactions
- Retrieves recent messages for context
- Saves user and AI messages to database

### MCP Tools
- `mcp_tools/todo_tool.py`: `manage_todo_mcp` - CRUD operations for tasks
- `mcp_tools/chat_memory_tool.py`: `sync_chat_memory` - Save/fetch chat history
- `mcp_tools/proactive_guard_tool.py`: `proactive_guard` - Duplicate/deadline validation
- `mcp_tools/handshake_tool.py`: `chat_handshake_mcp` - Initialize conversation context

### MCP Server
- `mcp_server.py`: Foundation for MCP server
- `main.py`: Entry point for the MCP server application

## Architecture

The system implements a stateless architecture where:
1. Each AI request triggers a "stateless handshake"
2. Recent chat history is retrieved from the database
3. Context is provided to the AI for informed responses
4. Both user input and AI responses are stored in the database

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment variables:
```bash
export COHERE_API_KEY="your-api-key"
export COHERE_MODEL="command-r-plus"
```

3. Start the MCP server:
```bash
cd phase3_ai_engine
python main.py --host localhost --port 8001
```

## Environment Variables

- `COHERE_API_KEY`: Your Cohere API key
- `COHERE_MODEL`: The model to use (default: command-r-plus)
- `DATABASE_URL`: PostgreSQL connection string