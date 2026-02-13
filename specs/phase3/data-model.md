# Phase 3: MCP Server - Data Model

## Database Schema

### chat_history Table
- **id**: UUID (Primary Key)
- **session_id**: String (Foreign Key to session)
- **role**: String (Values: "user", "assistant")
- **content**: Text (Conversation content)
- **created_at**: Timestamp (Creation time)

### sessions Table
- **id**: UUID (Primary Key)
- **user_id**: String (User identifier)
- **created_at**: Timestamp (Creation time)
- **last_active**: Timestamp (Last activity)

### todo_items Table
- **id**: UUID (Primary Key)
- **content**: Text (Todo item content)
- **status**: String (Values: "pending", "completed")
- **created_at**: Timestamp (Creation time)
- **updated_at**: Timestamp (Last update)
- **session_id**: String (Foreign Key to session)

## Relationships
- Sessions have many ChatMessages
- Sessions have many TodoItems
- TodoItems belong to a Session
- ChatMessages belong to a Session