# ADR-004: Data Architecture and Database Strategy

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Data Strategy" not separate ADRs for database, ORM, indexing).

- **Status:** Accepted
- **Date:** 2026-01-09
- **Feature:** phase2-web
- **Context:** Need to implement a reliable, scalable data architecture that supports the multi-user todo application with proper user isolation and efficient querying.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

Selected Neon Serverless PostgreSQL as the database with SQLModel ORM for data access. This strategy provides a robust solution for data persistence with proper user isolation and efficient querying capabilities.

- Database: Neon Serverless PostgreSQL
- ORM: SQLModel (integration with SQLAlchemy and Pydantic)
- User Isolation: Foreign key relationships with user_id filtering
- Indexing: Strategic indexes on user_id and completed fields
- Schema Management: SQLModel-based migrations

## Consequences

### Positive

- Serverless PostgreSQL provides auto-scaling and cost efficiency
- SQLModel provides excellent type safety with Python type hints
- Compatibility with both SQLAlchemy and Pydantic ecosystems
- Proper user isolation through foreign key relationships
- Efficient querying with strategic indexing
- ACID compliance and data integrity guarantees

### Negative

- Dependency on Neon cloud platform
- Learning curve for SQLModel if unfamiliar with SQLAlchemy
- Additional complexity compared to NoSQL alternatives
- Cost considerations with PostgreSQL usage

## Alternatives Considered

Alternative Strategy A: Raw SQL queries with psycopg
- Why rejected: Less safe, more error-prone, missing ORM benefits

Alternative Strategy B: SQLAlchemy Core + separate validation layer
- Why rejected: Missing Pydantic integration benefits, more complex setup

Alternative Strategy C: Alternative ORMs (Tortoise ORM, Databases)
- Why rejected: Less mature ecosystem, reduced compatibility with FastAPI

## References

- Feature Spec: specs/phase2-web/spec.md
- Implementation Plan: specs/phase2-web/plan.md
- Related ADRs:
- Evaluator Evidence: specs/phase2-web/research.md