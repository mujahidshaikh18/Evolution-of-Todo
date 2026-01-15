<!-- SYNC IMPACT REPORT
Version change: 1.3.0 → 2.0.0
Modified principles: Complete overhaul from Phase I specific to multi-phase global constitution
Added sections: All 5 phases architecture, tech stacks, security standards, testing strategy
Removed sections: Phase I specific limitations (replaced with multi-phase framework)
Templates requiring updates:
- ⚠️ .specify/templates/plan-template.md - Needs multi-phase guidelines
- ⚠️ .specify/templates/spec-template.md - Needs multi-phase structure
- ⚠️ .specify/templates/tasks-template.md - Needs multi-phase task types
Follow-up TODOs: Update templates to match new global constitution
-->

# Todo App Evolution - From CLI to Cloud-Native AI System Constitution

## Core Principles (Universal)

### I. Spec-Driven Development
ALL code generated through Claude Code based on specifications - zero manual coding. All development follows a strict specification-driven approach where requirements are captured in structured specifications before implementation. Every feature must have a corresponding specification document that defines WHAT needs to be built before determining HOW to build it.

### II. Progressive Enhancement
Each phase builds on previous phase without breaking existing functionality. Solutions must evolve from simple to complex implementations while maintaining backward compatibility where possible.

### III. Clean Architecture
Maintain clear separation of concerns (presentation, business logic, data). Each component should have a single responsibility and be easily testable in isolation. Architecture should be designed to accommodate evolution from simple to complex implementations.

### IV. Production Quality
Every phase must be deployable and demonstrable. All implementations must meet production standards appropriate for their phase while maintaining high quality and reliability.

### V. Documentation First
Specs before code, README before deployment. All development must be thoroughly documented with specifications, implementation details, and usage instructions.

## Key Standards

### Development Workflow (All Phases)
- MUST write Constitution once (this file, covers all phases)
- MUST write specifications before implementation
- MUST document all Claude Code prompts and iterations in /specs folder
- MUST refine specs when output is incorrect (never manually fix code)
- CANNOT skip phases or implement features from future phases early

### Code Quality (All Phases)
- Type hints mandatory (Python: mypy strict, TypeScript: strict mode)
- Docstrings/comments for public APIs
- Error handling: graceful failures with user-friendly messages
- Validation: all inputs validated before processing
- No silent failures or ignored errors
- Single Responsibility Principle for all functions/classes

## Phase-Specific Tech Stack

### Phase I - Console App
- **Language**: Python 3.13+
- **Package Manager**: UV
- **Storage**: In-memory (list/dict)
- **Interface**: CLI only
- **Dependencies**: Standard library preferred

### Phase II - Full-Stack Web
- **Frontend**: Next.js 16+ (App Router), TypeScript, Tailwind CSS
- **Backend**: Python FastAPI, SQLModel ORM
- **Database**: Neon Serverless PostgreSQL
- **Authentication**: Better Auth with JWT tokens
- **API Style**: RESTful JSON
- **Deployment**: Vercel (frontend), Backend hosted separately

### Phase III - AI Chatbot
- **Chat UI**: OpenAI ChatKit
- **AI Framework**: OpenAI Agents SDK
- **MCP Server**: Official MCP SDK (Python)
- **Architecture**: Stateless backend with DB persistence
- **Storage**: Conversations and messages in Neon DB
- **Natural Language**: User intents parsed by AI agent

### Phase IV - Local Kubernetes
- **Containerization**: Docker (use Docker AI/Gordon if available)
- **Orchestration**: Kubernetes via Minikube
- **Package Manager**: Helm Charts
- **AIOps Tools**: kubectl-ai, kagent for intelligent operations
- **Deployment**: Local cluster only

### Phase V - Cloud Production
- **Cloud Platform**: Azure AKS / Google GKE / Oracle OKE
- **Event Streaming**: Kafka (self-hosted via Strimzi OR Redpanda Cloud)
- **Distributed Runtime**: Dapr (Pub/Sub, State, Bindings, Secrets, Service Invocation)
- **CI/CD**: GitHub Actions
- **Monitoring**: Basic logging and health checks
- **Features**: Advanced Level (recurring tasks, due dates, reminders, priorities, tags)

## Architecture Principles

### Phase I Architecture
- Layered architecture: CLI → Business Logic → Data
- In-memory data structures
- Synchronous operations

### Phase II Architecture
- Monorepo structure (frontend + backend)
- RESTful API with user isolation (JWT-based)
- Stateless backend
- Database as single source of truth

### Phase III Architecture
- MCP tools expose backend operations to AI agent
- Stateless chat endpoint (state in DB)
- AI agent chains MCP tools for complex operations
- Conversation history persisted per user

### Phase IV Architecture
- Microservices architecture (frontend, backend, MCP server as separate pods)
- Service discovery via Kubernetes DNS
- ConfigMaps for configuration
- Secrets for sensitive data

### Phase V Architecture
- Event-Driven Architecture (Kafka topics: task-events, reminders, task-updates)
- Dapr sidecars for all services
- Pub/Sub abstraction via Dapr
- Async processing for notifications and recurring tasks
- Horizontal pod autoscaling

## Security Standards

### Authentication & Authorization (Phase II+)
- Better Auth for user authentication
- JWT tokens for API authorization
- User isolation: users only see their own data
- Token expiry: 7 days default
- Secure secret management (env vars Phase II-III, K8s secrets Phase IV+)

### API Security (Phase II+)
- All endpoints require authentication (except public health checks)
- Input validation on all endpoints
- SQL injection prevention via ORM (SQLModel)
- CORS properly configured
- HTTPS in production (Phase V)

### Data Privacy
- User data isolated by user_id
- No cross-user data leakage
- Passwords hashed (handled by Better Auth)
- API keys never committed to Git

## Testing Strategy

### Phase I Testing
- Manual testing (document test scenarios in specs)

### Phase II+ Testing
- Automated testing encouraged but not required for hackathon
- Unit tests for business logic
- Integration tests for API endpoints
- E2E tests for critical user flows

## Documentation Requirements (All Phases)

### README.md Requirements
- Project overview and current phase
- Tech stack for current phase
- Prerequisites (Python 3.13+, Node.js, Docker, etc.)
- Installation steps (detailed)
- Usage instructions with examples
- API documentation (Phase II+)
- Deployment instructions (Phase IV+)

### CLAUDE.md Requirements
- Spec-Kit Plus workflow explanation
- Example prompts and iterations
- How to navigate monorepo (Phase II+)
- MCP server usage (Phase III+)

### Specs Folder Requirements
- constitution.md (this file)
- specify.md (WHAT to build)
- plan.md (HOW to build)
- tasks.md (breakdown of work)
- Feature specifications organized by phase
- Architecture decision records

## Constraints (All Phases)

### Feature Progression
- Phase I: Basic Level only (Add, Delete, Update, View, Mark Complete)
- Phase II: Basic Level as web app + Authentication
- Phase III: Basic Level via AI chatbot + MCP tools
- Phase IV: Deploy Phase III to local Kubernetes
- Phase V: Add Intermediate + Advanced features + Event-driven + Cloud deployment

### Prohibited Practices (All Phases)
- Skipping specification phase
- Implementing features from future phases prematurely
- Using technologies not specified in phase requirements

## Success Criteria (Phase by Phase)

### Phase I Success Criteria
- Console app runs, all 5 features work, specs documented

### Phase II Success Criteria
- Web app deployed, multi-user with auth, REST API functional

### Phase III Success Criteria
- Chatbot responds to natural language, MCP tools work, stateless architecture

### Phase IV Success Criteria
- Running on Minikube, Helm charts created, kubectl-ai used

### Phase V Success Criteria
- Cloud deployment functional, event-driven features working, advanced capabilities

## Governance

This constitution governs all phases of the Todo App Evolution project (from CLI to Cloud-Native AI System). Principles remain consistent across phases while allowing for appropriate implementation variations based on phase-specific requirements. All code generated for any phase must comply with these requirements. Phase-specific variations must be documented in corresponding specification files. Amendments to this constitution require documentation of impact on existing work across all phases and approval from project maintainers.

For development guidance, follow the established patterns in this constitution and ensure all implementation aligns with the specified technology stack and architecture constraints while allowing for appropriate evolution between phases.

**Version**: 2.0.0 | **Ratified**: 2026-01-07 | **Last Amended**: 2026-01-07