---
name: console-app-overview
category: Phase I Skills
description: Overview of the Console App development process using the Console App Agent and its subagents. This provides a complete guide to building Python command-line applications with in-memory storage using Python 3.13+, implementing in-memory data models, and providing CRUD operations.
usage: /console-app-overview [options]
examples:
  - "/console-app-overview - Get an overview of console app development process"
  - "/console-app-overview 'Start building a todo CLI app' - Guide to creating CLI with in-memory storage"
  - "/console-app-overview 'Build a task manager CLI' - Complete workflow for CLI development"
model: sonnet
---

## Console App Development Overview

This document provides an overview of the Console App development process using the Console App Agent and its subagents. The process involves creating CLI applications using Python 3.13+, implementing in-memory data models, and providing comprehensive CRUD operations.

### Development Process

The Console App development process involves three main subagents working together:

1. **Python CLI Subagent**: Handles argparse/click interfaces for creating intuitive command-line interfaces, implementing proper argument parsing, and generating help text and documentation.

2. **Data Structure Subagent**: Designs in-memory data models for Python command-line applications, creating efficient data structures, implementing data validation, and ensuring data integrity in memory.

3. **CRUD Operations Subagent**: Implements add/delete/update/view/complete operations for Python command-line applications, providing comprehensive data manipulation capabilities with proper validation and error handling.

### When to Use
- When starting development of a Python CLI application
- When building applications with in-memory storage
- When implementing CRUD operations for console apps
- When managing dependencies with UV package manager
- When ensuring reusability across CLI projects

### Workflow
1. **Initialize Project**: Set up project structure with proper dependencies using UV
2. **Design Data Models**: Create in-memory data structures with validation
3. **Build CLI Interface**: Implement command-line interface with argparse/Click
4. **Implement CRUD Operations**: Add create, read, update, delete functionality
5. **Test and Validate**: Ensure proper error handling and user experience

### Best Practices
- Follow Python 3.13+ standards and conventions
- Implement proper error handling and logging
- Include comprehensive documentation
- Maintain clean, readable code structure
- Use reusable CLI patterns
- Optimize for in-memory performance
- Ensure proper project structure with pyproject.toml
- Include proper virtual environment setup