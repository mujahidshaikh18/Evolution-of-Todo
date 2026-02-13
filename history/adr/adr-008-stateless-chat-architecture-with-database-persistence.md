# ADR-008: Stateless Chat Architecture with Database Persistence

## Status
Accepted

## Date
2026-02-03

## Context
The system needs to maintain conversation history for context while maintaining a stateless architecture. We need to decide how to store and retrieve chat history to enable the "stateless handshake" pattern where each request first retrieves relevant conversation context from the database rather than relying on server-side session state.

## Decision
We will implement a stateless architecture where all chat history is stored in the database using a `chat_history` table with UUID, role, content, session_id, and created_at fields. Each request will retrieve the last 10-15 messages before sending to the AI to maintain context window efficiency.

### Components
- **Storage**: Neon PostgreSQL `chat_history` table
- **Fields**: id (UUID), session_id, role, content, created_at
- **Indexes**: Optimized for session-based and chronological queries
- **Context Window**: Retrieve last 10-15 messages per request

## Alternatives Considered

### Server-Side Session Storage
- **Pros**: Faster access, simpler implementation, less database load
- **Cons**: Violates stateless requirement, scaling challenges, session management complexity

### Redis/Memory Cache
- **Pros**: Fast access, supports TTL, good for temporary storage
- **Cons**: Still introduces state, additional infrastructure, potential data loss

### Client-Side Storage
- **Pros**: Truly stateless, reduces server load
- **Cons**: Security concerns, limited storage capacity, client dependency

### Hybrid Approach (Cache + Database)
- **Pros**: Best performance, fallback consistency
- **Cons**: Complexity, cache invalidation challenges, increased maintenance

## Consequences

### Positive
- True stateless architecture supporting horizontal scaling
- Persistent conversation history across server restarts
- Consistent user experience regardless of server instance
- Audit trail of all interactions
- Efficient retrieval with proper indexing

### Negative
- Additional database queries per AI request
- Potential performance impact from history retrieval
- Larger database storage requirements
- More complex data management and retention policies

## References
- specs/phase3/plan.md
- specs/phase3/spec.md