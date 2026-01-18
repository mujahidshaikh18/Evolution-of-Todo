# ADR-002: Backend Technology Stack

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Backend Stack" not separate ADRs for framework, ORM, deployment).

- **Status:** Accepted
- **Date:** 2026-01-09
- **Feature:** phase2-web
- **Context:** Need to select a modern, Python-based backend stack that integrates well with the frontend, provides type safety, and supports the required API patterns for the todo application.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

Selected FastAPI as the web framework combined with SQLModel ORM for database operations and Python 3.11+ as the runtime. This stack provides a cohesive solution for building the REST API backend.

- Framework: FastAPI 0.104+
- Language: Python 3.11+
- ORM: SQLModel 0.0.16+
- Type Safety: Pydantic integration through SQLModel
- Middleware: Built-in FastAPI middleware ecosystem

## Consequences

### Positive

- Automatic API documentation generation with Swagger/OpenAPI
- Excellent type safety through Python type hints and Pydantic
- High performance compared to traditional Python frameworks
- Easy validation and serialization with Pydantic
- Strong integration between FastAPI and SQLModel
- Asynchronous support for improved concurrency

### Negative

- Learning curve for developers unfamiliar with Python type hints
- Smaller ecosystem compared to Django for certain features
- FastAPI is relatively newer with evolving best practices
- Potential performance overhead for simple operations

## Alternatives Considered

Alternative Stack A: Django + DRF + standard ORM
- Why rejected: Heavier framework, more boilerplate, less aligned with API-first approach

Alternative Stack B: Flask + SQLAlchemy + Marshmallow
- Why rejected: More manual work required for validation and documentation

Alternative Stack C: Starlette + raw SQL
- Why rejected: Missing ORM benefits, more error-prone, no automatic validation

## References

- Feature Spec: specs/phase2-web/spec.md
- Implementation Plan: specs/phase2-web/plan.md
- Related ADRs:
- Evaluator Evidence: specs/phase2-web/research.md