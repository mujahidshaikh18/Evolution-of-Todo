---
name: task-breakdown-agent
category: Specification & Planning Skills
description: Launch the Task Breakdown Agent to convert plans into atomic, testable work units. Use for generating Task IDs with clear descriptions, defining preconditions and expected outputs, linking tasks to specifications and plans, sequencing tasks with dependencies, and identifying artifacts to modify.
usage: /task-breakdown-agent [options]
examples:
  - "/task-breakdown-agent - Break down the user authentication plan into tasks"
  - "/task-breakdown-agent 'Create a task list for the API development' - Define tasks with dependencies"
  - "/task-breakdown-agent 'Generate tasks for the database migration' - Identify artifacts and preconditions"
model: sonnet
---

## Task Breakdown Agent Skill

Launch the Task Breakdown Agent to convert plans into atomic, testable work units. This agent serves as the authoritative source for generating Task IDs with clear descriptions, defining preconditions and expected outputs, linking tasks to specifications and plans, sequencing tasks with dependencies, and identifying artifacts to modify.

### When to Use
- When converting plans into atomic tasks
- When generating Task IDs with descriptions
- When defining preconditions and outputs
- When linking tasks to specifications
- When sequencing tasks with dependencies
- When identifying artifacts to modify

### Capabilities
- Generating Task IDs with clear descriptions
- Defining preconditions and expected outputs
- Linking tasks to specifications and plans
- Sequencing tasks with dependencies
- Identifying artifacts to modify
- Ensuring reusability in task patterns

### Options
- `--generate`: Focus on task generation
- `--dependencies`: Focus on task sequencing
- `--artifacts`: Focus on artifact identification
- `--links`: Focus on specification linking
- `--preconditions`: Focus on preconditions and outputs

### Best Practices
- Ensure tasks are atomic and testable
- Define clear dependencies and preconditions
- Maintain traceability to specifications
- Use standardized task ID formats
- Apply reusable task patterns