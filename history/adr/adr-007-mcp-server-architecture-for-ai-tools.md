# ADR-007: MCP Server Architecture for AI Tools

## Status
Accepted

## Date
2026-02-03

## Context
The system needs to expose AI-powered functionality through MCP (Model Context Protocol) tools that can be invoked by the AI agent. We need to decide how to structure and deploy the MCP server in relation to the existing backend. The requirements include exposing todo management, chat memory sync, and proactive guard functionality as MCP tools.

## Decision
We will create a separate MCP server application in the `phase3_ai_engine` directory that runs independently from the main backend. This server will expose multiple MCP tools including `manage_todo_mcp`, `sync_chat_memory`, `proactive_guard`, and `chat_handshake_mcp`.

### Components
- **MCP Server Location**: `/phase3_ai_engine/` directory
- **Tool Types**: Four main MCP tools for different functionalities
- **Deployment**: Separate service running on different port
- **Communication**: Standard MCP protocol for AI integration

## Alternatives Considered

### Integrated MCP Tools in Backend
- **Pros**: Simpler deployment, shared authentication, fewer moving parts
- **Cons**: Tight coupling between AI tools and backend, potential performance issues, harder to evolve independently

### Microservice Architecture
- **Pros**: Maximum flexibility, independent scaling, clear separation of concerns
- **Cons**: Increased complexity, additional operational overhead, more network calls

### Client-Side MCP Tools
- **Pros**: Reduced server load, direct client integration
- **Cons**: Security concerns, inconsistent user experience, harder to maintain

## Consequences

### Positive
- Clear separation between AI tools and main backend functionality
- Independent development and deployment cycles
- Standardized MCP interface for AI integration
- Reusable tools that can be consumed by multiple AI agents

### Negative
- Additional service to monitor and maintain
- Extra network hops between services
- More complex debugging and troubleshooting
- Potential for service availability issues affecting AI functionality

## References
- specs/phase3/plan.md
- specs/phase3/spec.md