import unittest
import pytest
from httpx import AsyncClient, ASGITransport
from unittest.mock import patch, MagicMock, AsyncMock
import sys
import os

# Path adjustment
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from main import app 
from middleware.auth import verify_jwt_token

# Mock token data
mock_token_data = {"user_id": "test_user", "username": "testuser"}

@pytest.fixture(autouse=True)
def override_auth_dependency():
    app.dependency_overrides[verify_jwt_token] = lambda: mock_token_data
    yield
    app.dependency_overrides = {}

@pytest.mark.asyncio
class TestChatEndpoint:
    """Async Integration tests - Final Fix for 500 Error"""

    async def test_chat_converse_endpoint(self):
        # 1. Patch the class normally (MagicMock)
        with patch('routes.chat.ChatService') as mock_chat_class, \
             patch('routes.chat.get_session') as mock_get_session, \
             patch('routes.chat.get_chat_handshake_mcp_tool') as mock_handshake_tool:

            # 2. Setup the INSTANCE of the service as AsyncMock
            mock_service_instance = AsyncMock()
            mock_service_instance.process_user_query.return_value = {
                "response": "Test AI response", 
                "tool_calls": []
            }
            
            mock_chat_class.return_value = mock_service_instance
            
            # 3. Setup Handshake Tool
            mock_handshake_instance = AsyncMock()
            mock_handshake_instance.execute.return_value = {"success": True, "recent_messages": []}
            mock_handshake_tool.return_value = mock_handshake_instance
            
            mock_get_session.return_value.__enter__.return_value = MagicMock()

            async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
                response = await ac.post(
                    "/api/chat/converse",
                    json={
                        "message": "Hello", 
                        "session_id": "test_sess", 
                        "user_id": "test_user"
                    }
                )

            if response.status_code != 200:
                print(f"Error Detail: {response.json()}")

            assert response.status_code == 200
            assert response.json()["response"] == "Test AI response"

    async def test_get_chat_history_endpoint(self):
        # Already passing, just keeping consistency
        with patch('routes.chat.ChatService') as mock_chat_class:
            mock_service_instance = AsyncMock()
            mock_service_instance.get_recent_messages.return_value = []
            mock_chat_class.return_value = mock_service_instance

            async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
                response = await ac.get("/api/chat/history/test_sess")
            assert response.status_code == 200

    async def test_chat_handshake_endpoint(self):
        # Already passing
        with patch('routes.chat.get_chat_handshake_mcp_tool') as mock_handshake_tool:
            mock_handshake_instance = AsyncMock()
            mock_handshake_instance.execute.return_value = {"success": True, "session_context": {}}
            mock_handshake_tool.return_value = mock_handshake_instance

            async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
                response = await ac.post(
                    "/api/chat/handshake",
                    json={"message": "", "session_id": "test_sess", "user_id": "test_user"}
                )
            assert response.status_code == 200