# ADR-005: API Design and Architecture

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "API Design" not separate ADRs for protocol, patterns, structure).

- **Status:** Accepted
- **Date:** 2026-01-09
- **Feature:** phase2-web
- **Context:** Need to design a RESTful API that supports the todo application features while ensuring proper user isolation and following industry standards.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

Selected RESTful JSON API with user_id in URL path as the primary design pattern. This approach provides clear resource identification and follows standard REST conventions while enabling proper user isolation.

- API Style: RESTful JSON
- Resource Identification: URL path with user_id
- Authentication: JWT tokens in Authorization header
- Error Handling: Standard HTTP status codes with JSON responses
- Validation: Request/response validation through Pydantic models

## Consequences

### Positive

- Follows standard REST conventions familiar to developers
- Clear resource identification and organization
- Proper user isolation through URL-based validation
- Standard HTTP status codes for predictable error handling
- Easy to document and test
- Good tooling support for REST APIs

### Negative

- Potential for URL complexity with user_id in path
- Less flexible than GraphQL for complex queries
- May require multiple requests for related resources
- Over-fetching potential compared to GraphQL

## Alternatives Considered

Alternative Approach A: GraphQL API
- Why rejected: More complex for basic todo functionality, unnecessary overhead for Phase II

Alternative Approach B: WebSocket-based real-time API
- Why rejected: Not required for basic functionality, adds complexity

Alternative Approach C: Serverless functions with user validation
- Why rejected: Would complicate user isolation implementation, less cohesive architecture

## References

- Feature Spec: specs/phase2-web/spec.md
- Implementation Plan: specs/phase2-web/plan.md
- Related ADRs:
- Evaluator Evidence: specs/phase2-web/research.md