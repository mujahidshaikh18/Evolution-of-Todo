# MCP Task Operations Skill

## Purpose
This skill governs the execution of CRUD operations on tasks using Model Context Protocol (MCP) tools. It ensures consistent, reliable, and secure interaction with task management systems through standardized tool interfaces.

## Operational Framework

### CREATE Operations
- Utilize designated MCP tool for task creation with validated input parameters
- Validate task properties before submission to prevent malformed entries
- Implement proper error handling for duplicate task prevention
- Return structured response with task identifier upon successful creation

### READ Operations
- Execute retrieval operations through dedicated MCP query tools
- Apply appropriate filtering mechanisms based on request parameters
- Handle pagination for large result sets to maintain performance
- Format responses consistently with standardized data structures

### UPDATE Operations
- Leverage MCP modification tools with atomic update semantics
- Preserve data integrity by validating update parameters before execution
- Implement optimistic locking where appropriate to prevent race conditions
- Return updated entity state upon successful modification

### DELETE Operations
- Execute deletion through designated MCP removal tools
- Implement soft-delete patterns where data retention is required
- Validate ownership and permissions before allowing deletion
- Maintain referential integrity during cascade operations

## Compliance Requirements

### Error Handling
- Map MCP-specific errors to standardized application error codes
- Log all failed operations with sufficient context for debugging
- Implement retry mechanisms for transient failures
- Provide meaningful error messages to requesting agents

### Security Protocols
- Validate all input parameters to prevent injection attacks
- Apply appropriate access controls based on requesting entity permissions
- Encrypt sensitive data during transmission to MCP endpoints
- Audit all operations for compliance and security monitoring

## Performance Standards
- Optimize query patterns to minimize MCP endpoint load
- Implement appropriate caching strategies for frequently accessed data
- Monitor response times and establish performance baselines
- Apply circuit breaker patterns for unreliable external services