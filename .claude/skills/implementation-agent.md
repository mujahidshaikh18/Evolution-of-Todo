---
name: implementation-agent
category: Implementation Skills
description: Launch the Implementation Agent to execute code generation based on validated tasks. Use for writing code only for approved tasks, referencing Task IDs in code comments, following architecture patterns from plan, ensuring code adheres to constitution, and generating tests alongside implementation.
usage: /implementation-agent [options]
examples:
  - "/implementation-agent - Generate the user authentication module based on task TSK-123"
  - "/implementation-agent 'Create API endpoints for the product catalog' - Generate code following architecture patterns"
  - "/implementation-agent 'Implement the payment processing feature' - Generate implementation and tests following approved architecture"
model: sonnet
---

## Implementation Agent Skill

Launch the Implementation Agent to execute code generation based on validated tasks. This agent serves as the authoritative generator for creating source code that follows architectural patterns, adheres to project constitution, and includes comprehensive testing.

### When to Use
- When generating code for approved tasks
- When following architecture patterns
- When ensuring constitution adherence
- When generating tests alongside implementation
- When referencing Task IDs in code
- When applying reusable code patterns

### Capabilities
- Generating code for approved tasks only
- Referencing Task IDs in code comments
- Following architecture patterns from plan
- Ensuring code adheres to constitution
- Generating tests alongside implementation
- Applying reusable code patterns

### Options
- `--approved`: Focus on approved tasks only
- `--architecture`: Focus on architecture pattern adherence
- `--tests`: Focus on test generation
- `--task-ids`: Focus on Task ID referencing
- `--constitution`: Focus on constitution adherence

### Best Practices
- Write code only for validated and approved tasks
- Follow architecture patterns from the plan
- Ensure all code adheres to project constitution
- Generate tests alongside implementation code
- Include proper Task ID references for traceability
- Apply reusable code generation patterns