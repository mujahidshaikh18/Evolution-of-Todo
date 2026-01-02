---
name: constitution-agent
category: Specification & Planning Skills
description: Launch the Constitution Agent to define, maintain, or enforce project-wide principles, constraints, and architectural guidelines. Use during project setup, architectural decision making, code reviews, and when establishing coding standards or tech stack constraints.
usage: /constitution-agent [options]
examples:
  - "/constitution-agent - Update coding standards for the project"
  - "/constitution-agent 'What are our security principles?' - Retrieve security guidelines"
  - "/constitution-agent 'Should we allow this new dependency?' - Check tech stack constraints"
model: sonnet
---

## Constitution Agent Skill

Launch the Constitution Agent to define, maintain, or enforce project-wide principles, constraints, and architectural guidelines. This agent serves as the authoritative source for project standards, coding conventions, security requirements, performance principles, and architectural boundaries.

### When to Use
- During project setup to define standards
- During architectural decision making
- During code reviews to check compliance
- When establishing coding standards
- When evaluating tech stack decisions
- When checking architectural constraints

### Capabilities
- Maintaining project constitution
- Enforcing coding standards
- Managing tech stack constraints
- Ensuring security & performance
- Guarding architectural boundaries
- Providing authoritative guidance

### Options
- `--update`: Update existing constitution elements
- `--check`: Check compliance against constitution
- `--new`: Create new constitution elements

### Best Practices
- Reference specific parts of the constitution when making decisions
- Suggest updates rather than making unilateral decisions when constitution is unclear
- Maintain consistency in application of principles