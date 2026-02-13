"""
MCP Tool for synchronizing chat memory with database
"""
import sys
from pathlib import Path
from typing import Dict, Any, List, Optional
from datetime import datetime
from sqlmodel import Session, select

# Add the backend path to sys.path to import models and db
backend_path = Path(__file__).parent.parent.parent / "todo-phase2" / "backend"
if str(backend_path) not in sys.path:
    sys.path.insert(0, str(backend_path))

# Now import from backend
from models import ChatHistory
from db import get_engine


class ChatMemoryMCPTask:
    def __init__(self):
        self.engine = get_engine()

    def execute(self, session_id: str, action: str, message_data: Optional[Dict[str, Any]] = None, limit: int = 10) -> Dict[str, Any]:
        """
        Execute chat memory operations

        Args:
            session_id: Identifier for the conversation session
            action: Action to perform (save, fetch, truncate)
            message_data: Message details for save operations
            limit: Limit for fetch operations

        Returns:
            Dictionary with operation result
        """
        with Session(self.engine) as db_session:
            try:
                if action == "save":
                    return self._save_message(db_session, session_id, message_data)
                elif action == "fetch":
                    return self._fetch_messages(db_session, session_id, limit)
                elif action == "truncate":
                    return self._truncate_messages(db_session, session_id)
                else:
                    raise ValueError(f"Unsupported action: {action}")
            except Exception as e:
                return {
                    "success": False,
                    "error": str(e),
                    "action": action
                }

    def _save_message(self, session: Session, session_id: str, message_data: Dict[str, Any]) -> Dict[str, Any]:
        """Save a message to the database"""
        if not message_data:
            raise ValueError("message_data is required for save operation")

        # Create chat history object
        chat_history = ChatHistory(
            session_id=session_id,
            role=message_data.get('role', ''),
            content=message_data.get('content', ''),
            created_at=datetime.utcnow()
        )

        # Add to session and commit
        session.add(chat_history)
        session.commit()
        session.refresh(chat_history)

        return {
            "success": True,
            "action": "save",
            "message_id": str(chat_history.id)
        }

    def _fetch_messages(self, session: Session, session_id: str, limit: int = 10) -> Dict[str, Any]:
        """Fetch recent messages from the database"""
        statement = (
            select(ChatHistory)
            .where(ChatHistory.session_id == session_id)
            .order_by(ChatHistory.created_at.desc())
            .limit(limit)
        )

        results = session.exec(statement).all()

        # Convert to message format
        messages = []
        for msg in reversed(results):  # Reverse to maintain chronological order
            messages.append({
                "id": str(msg.id),
                "role": msg.role,
                "content": msg.content,
                "created_at": msg.created_at.isoformat() if hasattr(msg.created_at, 'isoformat') else str(msg.created_at)
            })

        return {
            "success": True,
            "action": "fetch",
            "messages": messages,
            "count": len(messages)
        }

    def _truncate_messages(self, session: Session, session_id: str) -> Dict[str, Any]:
        """Truncate messages for a session (clear conversation history)"""
        statement = select(ChatHistory).where(ChatHistory.session_id == session_id)
        results = session.exec(statement).all()

        deleted_count = 0
        for msg in results:
            session.delete(msg)
            deleted_count += 1

        session.commit()

        return {
            "success": True,
            "action": "truncate",
            "deleted_count": deleted_count
        }


# Global instance
chat_memory_mcp_tool = ChatMemoryMCPTask()


def get_chat_memory_mcp_tool():
    """Get the global chat memory MCP tool instance"""
    return chat_memory_mcp_tool