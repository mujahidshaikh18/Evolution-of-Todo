"""
MCP Tool for performing chat handshake and initializing conversation context
"""
import sys
from typing import Dict, Any, List, Optional
from datetime import datetime
from pathlib import Path
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select

# Add the project root to the Python path to enable proper imports
project_root = Path(__file__).parent.parent.parent

# Add the backend path to sys.path to import models and db
backend_path = project_root / "todo-phase2" / "backend"
for path in [str(project_root), str(backend_path)]:
    if path not in sys.path:
        sys.path.insert(0, path)

# Import from the local models and db since they're now in path
from models import ChatHistory
from db import get_engine


class ChatHandshakeMCPTask:
    def __init__(self):
        self.engine = get_engine()

    async def execute(self, session_id: str, user_id: str, context_size: int = 10) -> Dict[str, Any]:
        """
        Execute the chat handshake to initialize conversation context

        Args:
            session_id: Conversation identifier
            user_id: User identifier
            context_size: Number of messages to retrieve for context

        Returns:
            Dictionary with recent chat messages and session context
        """
        async with AsyncSession(self.engine) as db_session:
            try:
                # Fetch recent messages for the session
                messages = await self._get_recent_messages(db_session, session_id, context_size)

                # Create session context
                session_context = {
                    "session_id": session_id,
                    "user_id": user_id,
                    "timestamp": datetime.utcnow().isoformat(),
                    "message_count": len(messages),
                    "context_size": context_size
                }

                return {
                    "success": True,
                    "session_context": session_context,
                    "recent_messages": messages
                }
            except Exception as e:
                return {
                    "success": False,
                    "error": str(e),
                    "session_id": session_id
                }

    async def _get_recent_messages(self, session: AsyncSession, session_id: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Retrieve recent messages for a session"""
        statement = (
            select(ChatHistory)
            .where(ChatHistory.session_id == session_id)
            .order_by(ChatHistory.created_at.desc())
            .limit(limit)
        )

        result = await session.exec(statement)
        results = result.all()

        # Convert to message format, reversing to maintain chronological order
        messages = []
        for msg in reversed(results):
            messages.append({
                "id": str(msg.id),
                "role": msg.role,
                "content": msg.content,
                "created_at": msg.created_at.isoformat() if hasattr(msg.created_at, 'isoformat') else str(msg.created_at)
            })

        return messages


# Global instance
chat_handshake_mcp_tool = ChatHandshakeMCPTask()


def get_chat_handshake_mcp_tool():
    """Get the global chat handshake MCP tool instance"""
    return chat_handshake_mcp_tool