import pytest
from unittest.mock import MagicMock, patch, AsyncMock
import sys
import os

# Add the project root to the Python path to enable proper imports
project_root = os.path.join(os.path.dirname(__file__), '..', '..')
phase3_ai_engine_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'phase3_ai_engine')

if project_root not in sys.path:
    sys.path.insert(0, project_root)
if phase3_ai_engine_path not in sys.path:
    sys.path.insert(0, phase3_ai_engine_path)

# Import the real ChatService and its dependencies
from phase3_ai_engine.services.chat_service import ChatService

class TestChatService:
    """Unit tests for ChatService - Ultimate Compatibility Version"""

    @pytest.mark.asyncio
    async def test_get_recent_messages(self):
        mock_session = AsyncMock() 
        mock_exec_result = MagicMock()
        mock_exec_result.all.return_value = []
        mock_session.exec.return_value = mock_exec_result

        with patch('phase3_ai_engine.services.chat_service.select') as mock_select:
            mock_select.return_value = MagicMock()
            service = ChatService(mock_session)
            result = await service.get_recent_messages("session_123", limit=5)
            assert result == []

    @pytest.mark.asyncio
    async def test_save_message(self):
        mock_session = AsyncMock()
        mock_session.commit = AsyncMock()
        service = ChatService(mock_session)

        with patch('phase3_ai_engine.services.chat_service.ChatHistory') as mock_chat_history:
            mock_message_instance = MagicMock()
            mock_chat_history.return_value = mock_message_instance
            await service.save_message("session_123", "user", "test message")
            
            mock_session.add.assert_called_once()
            assert mock_session.commit.called

    @pytest.mark.asyncio
    async def test_process_user_query(self):

        mock_session = AsyncMock()
        service = ChatService(mock_session)
        service.ai_client = AsyncMock()
        service.todo_tool = AsyncMock()

        # Mock the AI client response
        mock_choice = MagicMock()
        mock_choice.message.content = "AI response"
        mock_ai_response = MagicMock()
        mock_ai_response.choices = [mock_choice]
        service.ai_client.chat_completion.return_value = mock_ai_response

        # Mocking all internal logic
        with patch.object(service, 'save_message', new_callable=AsyncMock), \
             patch.object(service, 'get_recent_messages', new_callable=AsyncMock) as mock_recent:

            mock_recent.return_value = []

            result = await service.process_user_query(
                session_id="session_123",
                user_input="user input",
                user_id="user_123"
            )

            # String or dict assertion
            assert "response" in result