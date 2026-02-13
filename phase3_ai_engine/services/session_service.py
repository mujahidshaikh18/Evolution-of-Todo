"""
Session management service for handling conversation sessions
"""
import uuid
import sys
from datetime import datetime
from pathlib import Path
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select

# Add the project root to the Python path to enable proper imports
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

# Add the backend path to sys.path to import models and db
backend_path = Path(__file__).parent.parent.parent / "todo-phase2" / "backend"
if str(backend_path) not in sys.path:
    sys.path.insert(0, str(backend_path))

# Import from the local models and db since they're now in path
from models import ChatHistory
from db import get_engine


class SessionService:
    def __init__(self):
        self.engine = get_engine()

    def create_session(self, user_id: str = None) -> str:
        """
        Create a new conversation session

        Args:
            user_id: Optional user identifier for session association

        Returns:
            Session ID as a string
        """
        session_id = str(uuid.uuid4())
        # In a real implementation, we might store session metadata in the database
        # For now, we just return a unique session ID
        return session_id

    async def get_session_context(self, session_id: str, context_size: int = 10) -> dict:
        """
        Get context for a specific session

        Args:
            session_id: Session identifier
            context_size: Number of recent messages to include

        Returns:
            Dictionary containing session context
        """
        async with AsyncSession(self.engine) as db_session:
            # Get recent messages for the session
            statement = (
                select(ChatHistory)
                .where(ChatHistory.session_id == session_id)
                .order_by(ChatHistory.created_at.desc())
                .limit(context_size)
            )

            result = await db_session.exec(statement)
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

            session_context = {
                "session_id": session_id,
                "message_count": len(messages),
                "context_size": context_size,
                "recent_messages": messages,
                "timestamp": datetime.utcnow().isoformat()
            }

            return session_context

    async def validate_session(self, session_id: str) -> bool:
        """
        Validate if a session exists and is active

        Args:
            session_id: Session identifier to validate

        Returns:
            Boolean indicating if session is valid
        """
        # For this implementation, we'll just check if there are messages for the session
        async with AsyncSession(self.engine) as db_session:
            statement = select(ChatHistory).where(ChatHistory.session_id == session_id).limit(1)
            result = await db_session.exec(statement)
            first_result = result.first()
            return first_result is not None

    async def clear_session_history(self, session_id: str) -> int:
        """
        Clear all messages for a session

        Args:
            session_id: Session identifier

        Returns:
            Number of deleted messages
        """
        async with AsyncSession(self.engine) as db_session:
            # Get all messages for the session
            statement = select(ChatHistory).where(ChatHistory.session_id == session_id)
            result = await db_session.exec(statement)
            results = result.all()

            # Delete each message
            deleted_count = 0
            for msg in results:
                await db_session.delete(msg)
                deleted_count += 1

            await db_session.commit()
            return deleted_count


# Global instance
session_service = SessionService()


def get_session_service():
    """Get the global session service instance"""
    return session_service