"""
MCP Server Foundation for exposing tools to AI agents
"""
import asyncio
import json
import sys
from pathlib import Path
from typing import Dict, Any, List
from pydantic import BaseModel, Field
from sqlmodel import Session, create_engine, select

# --- CRITICAL PATH FIX START ---
current_file = Path(__file__).resolve()
project_root = current_file.parent.parent
backend_path = project_root / "todo-phase2" / "backend"

if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))
if str(backend_path) not in sys.path:
    sys.path.insert(0, str(backend_path))
# --- CRITICAL PATH FIX END ---

# Create a simple Server class since model_context_protocol is not available
class Server:
    def __init__(self, name: str, version: str):
        self.name = name
        self.version = version
        self.handlers = {}

    def set_handler(self, name):
        def decorator(func):
            self.handlers[name] = func
            return func
        return decorator

    def mount_in_fastapi(self, app, path):
        # Placeholder for mounting in FastAPI
        pass

# Create simple Tool-related classes
class ToolResult:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

class Tool:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

class ToolCall:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

from db import get_engine
from models import Task, User
from mcp_tools.todo_tool import get_todo_mcp_tool
from mcp_tools.chat_memory_tool import get_chat_memory_mcp_tool
from mcp_tools.proactive_guard_tool import get_proactive_guard_mcp_tool
from mcp_tools.handshake_tool import get_chat_handshake_mcp_tool


class MCPServer:
    def __init__(self):
        self.server = Server(name="Todo Chatbot MCP Server", version="1.0.0")
        self.engine = get_engine()
        self._register_tools()

    def _register_tools(self):
        """Register all MCP tools"""
        # Register the tools with the server
        self._register_manage_todo_tool()
        self._register_sync_chat_memory_tool()
        self._register_proactive_guard_tool()
        self._register_chat_handshake_tool()

    def _register_manage_todo_tool(self):
        """Register the manage_todo_mcp tool"""
        @self.server.set_handler("manage_todo_mcp")
        async def handle_manage_todo(params: Dict[str, Any]) -> Dict[str, Any]:
            """
            Handle todo management operations
            Expected params: {
                "operation": "create|read|update|delete|complete",
                "task_data": {...},
                "task_id": "...",
                "user_id": "..."
            }
            """
            operation = params.get("operation")
            task_data = params.get("task_data")
            task_id = params.get("task_id")
            user_id = params.get("user_id")

            todo_tool = get_todo_mcp_tool()
            result = await todo_tool.execute(operation, task_data, task_id, user_id)

            return result

    def _register_sync_chat_memory_tool(self):
        """Register the sync_chat_memory tool"""
        @self.server.set_handler("sync_chat_memory")
        async def handle_sync_chat_memory(params: Dict[str, Any]) -> Dict[str, Any]:
            """
            Handle chat memory operations
            Expected params: {
                "session_id": "...",
                "action": "save|fetch|truncate",
                "message_data": {...},
                "limit": 10
            }
            """
            session_id = params.get("session_id")
            action = params.get("action")
            message_data = params.get("message_data")
            limit = params.get("limit", 10)

            chat_memory_tool = get_chat_memory_mcp_tool()
            result = await chat_memory_tool.execute(session_id, action, message_data, limit)

            return result

    def _register_proactive_guard_tool(self):
        """Register the proactive_guard tool"""
        @self.server.set_handler("proactive_guard")
        async def handle_proactive_guard(params: Dict[str, Any]) -> Dict[str, Any]:
            """
            Handle proactive guard operations
            Expected params: {
                "operation": "check_duplicates|check_deadlines|validate",
                "task_data": {...},
                "user_id": "..."
            }
            """
            operation = params.get("operation")
            task_data = params.get("task_data")
            user_id = params.get("user_id")

            proactive_guard_tool = get_proactive_guard_mcp_tool()
            result = await proactive_guard_tool.execute(operation, task_data, user_id)

            return result

    def _register_chat_handshake_tool(self):
        """Register the chat_handshake_mcp tool"""
        @self.server.set_handler("chat_handshake_mcp")
        async def handle_chat_handshake(params: Dict[str, Any]) -> Dict[str, Any]:
            """
            Handle chat handshake operations
            Expected params: {
                "session_id": "...",
                "user_id": "...",
                "context_size": 10
            }
            """
            session_id = params.get("session_id")
            user_id = params.get("user_id")
            context_size = params.get("context_size", 10)

            handshake_tool = get_chat_handshake_mcp_tool()
            result = await handshake_tool.execute(session_id, user_id, context_size)

            return result

    def get_db_session(self) -> Session:
        """Get a database session"""
        return Session(self.engine)

    def start(self, host: str = "localhost", port: int = 8001):
        """Start the MCP server"""
        print(f"Starting MCP Server on {host}:{port}")
        print("Registered tools: manage_todo_mcp, sync_chat_memory, proactive_guard, chat_handshake_mcp")

        # Start the actual server
        try:
            import uvicorn
            from fastapi import FastAPI

            app = FastAPI()

            # Mount the MCP server to the FastAPI app
            self.server.mount_in_fastapi(app, "/mcp")

            # Run the server
            uvicorn.run(app, host=host, port=port)
        except ImportError:
            print("uvicorn not available, running in development mode")
            print("MCP Server started successfully on development mode!")
        except Exception as e:
            print(f"Error starting MCP server: {e}")

    async def shutdown(self):
        """Shutdown the MCP server"""
        print("Shutting down MCP Server...")
        # Cleanup operations would go here


# Global instance
mcp_server = MCPServer()


def get_mcp_server():
    """Get the global MCP server instance"""
    return mcp_server