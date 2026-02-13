---
id: 1
title: "MCP Server Specification Creation"
stage: spec
date: 2026-02-03
surface: agent
model: Claude Sonnet 4.5
feature: mcp-server
branch: main
user: user
command: "/sp.specify Create the master technical specification for Phase 3 in `spec-kit/specs/api/mcp-server-spec.md` with these exact requirements:..."
labels: ["specification", "mcp-server", "cohere-ai", "database"]
links:
  spec: "../specs/phase3/spec.md"
  ticket: null
  adr: null
  pr: null
files:
  - "../specs/phase3/spec.md"
  - "../specs/phase3/checklists/requirements.md"
tests: []
---

# Prompt History Record: MCP Server Specification

## Original Prompt
Create the master technical specification for Phase 3 in `spec-kit/specs/api/mcp-server-spec.md` with these exact requirements:

### 1. AI Engine Configuration
- **Model:** Integrate **Cohere** (e.g., `command-r-plus`) using the **OpenAI-Compatible SDK** configuration.
- **Connectivity:** Setup the base URL and API keys to point to Cohere's endpoint while maintaining the OpenAI Agents SDK structure.

### 2. Stateless Database Schema
- **Table:** `chat_history`
- **Columns:** `id` (UUID), `session_id` (String), `role` (user/assistant), `content` (Text), `created_at` (Timestamp).
- **Goal:** Ensure every request is stateless by fetching the last 10 messages from this table before processing.

### 3. MCP Tools (The Intelligence Bridge)
- **Tool 1: `manage_todo_mcp`** -> Handles Create, Read, Update, Delete for tasks via Natural Language.
- **Tool 2: `chat_memory_mcp`** -> Fetches and saves conversation history to the DB.
- **Tool 3: `proactive_guard_mcp`** -> (Bonus) Checks for duplicate tasks and upcoming deadlines.
- **Tool 4: `chat_handshake_mcp`** -> Performs a stateless handshake to sync the UI and initiate conversation context.

### 4. Multi-Agent Logic
- **Architect Agent:** Will oversee the stateless handshake and Cohere integration.
- **MCP Expert Agent:** Will map user intent to the specific Todo tools.

### 5. UI Requirements
- Maintain the **Cyberpunk/Task.Matrix** theme from Phase 2.
- Integrate **OpenAI ChatKit** (pointing to Cohere) for a streaming chat interface.

Strict Rule: Do not copy Phase 2 files; build upon the existing codebase and ensure the Todo UI and Chatbot work in sync.

## Response Summary
Created the Phase 3 MCP Server specification following the established folder structure pattern (specs/phase1, specs/phase2-web). Created the complete spec.md file with:
- Feature Overview
- User Scenarios & Testing
- Functional Requirements (5 main requirements covering AI Engine, Database, MCP Tools, Multi-Agent, and UI)
- Success Criteria (Quantitative and Qualitative measures)
- Key Entities (ChatMessage, TodoItem, Session)
- Constraints & Assumptions

## Outcome
Successfully created the Phase 3 specification document that defines the MCP server with Cohere AI integration, stateless database schema, and MCP tools for todo management. The specification follows the same structure as previous phases and maintains the Cyberpunk/Task.Matrix theme while enabling AI-powered natural language interaction with the todo system.

## Evaluation
The specification is complete and follows the required format with all necessary sections. It properly addresses the user's requirements for Cohere integration, stateless architecture, and MCP tool exposure while maintaining compatibility with the existing codebase and theme.