"""
Chat endpoint with stateless handshake for Cohere integration
"""
from fastapi import APIRouter, HTTPException, Depends
from typing import Dict, Any, List, Optional
from pydantic import BaseModel
from sqlmodel.ext.asyncio.session import AsyncSession
from db import get_session
from middleware.auth import verify_jwt_token
from phase3_ai_engine.services.chat_service import ChatService
from phase3_ai_engine.mcp_tools.handshake_tool import get_chat_handshake_mcp_tool
from datetime import datetime, timezone


router = APIRouter(prefix="/api/chat", tags=["chat"])


class ChatRequest(BaseModel):
    message: str
    session_id: str
    user_id: str


class ChatResponse(BaseModel):
    response: str
    session_id: str
    timestamp: str
    tool_calls: List[Dict[str, Any]] = []
    tool_results: List[Dict[str, Any]] = []
    refresh_tasks: bool = False


@router.post("/converse", response_model=ChatResponse)
async def chat_converse(
    request: ChatRequest,
    db_session: AsyncSession = Depends(get_session),
    token_data: dict = Depends(verify_jwt_token)
):
    """
    Handle chat conversation with stateless handshake

    This endpoint implements the 'stateless handshake' pattern:
    1. First, it retrieves the recent chat history for the session
    2. Then sends the user's message along with context to Cohere
    3. Saves both user message and AI response to database
    """
    try:
        # Validate that the user_id in the request matches the authenticated user
        user_id = token_data.get("user_id")
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token: User ID missing")

        # Perform stateless handshake - get recent messages for context
        handshake_tool = get_chat_handshake_mcp_tool()
        handshake_result = await handshake_tool.execute(
            session_id=request.session_id,
            user_id=user_id,
            #context_size=10 # Retrieve last 10 messages for context
        )

        if not handshake_result.get("success"):
            raise HTTPException(status_code=500, detail="Failed to retrieve chat context")

        # Create chat service instance
        chat_service = ChatService(db_session)

        # Process user query with AI and tool execution
        result = await chat_service.process_user_query(
            session_id=request.session_id,
            user_input=request.message,
            user_id=user_id,
            #context_size=10
        )
        current_time = datetime.now(timezone.utc).isoformat()

        # Use the refresh_tasks flag from the result
        refresh_tasks = result.get("refresh_tasks", False)

        # Prepare response
        response = ChatResponse(
            response=result["response"],
            session_id=request.session_id,
            timestamp=current_time,
            tool_calls=result.get("tool_calls", []),
            tool_results=result.get("tool_results", []),
            refresh_tasks=refresh_tasks
        )

        return response

    except HTTPException:
        raise  # Re-raise HTTP exceptions as-is
    except Exception as e:
        print(f"!!! ROUTE ERROR !!!: {str(e)}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Chat processing error: {str(e)}")


@router.get("/history/{session_id}")
async def get_chat_history(
    session_id: str,
    limit: int = 3,
    db_session: AsyncSession = Depends(get_session),
    token_data: dict = Depends(verify_jwt_token)
):
    """
    Retrieve chat history for a specific session
    """
    try:
        # In a real implementation, you'd validate that the session belongs to the user
        # For now, we'll trust the session_id but ensure the user is authenticated

        # Use the chat service to get recent messages
        chat_service = ChatService(db_session)
        messages = await chat_service.get_recent_messages(session_id, limit)

        return {
            "session_id": session_id,
            "messages": messages,
            "count": len(messages)
        }
    except HTTPException:
        raise  # Re-raise HTTP exceptions as-is
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve chat history: {str(e)}")


@router.post("/handshake")
async def chat_handshake(
    request: ChatRequest,
    db_session: AsyncSession = Depends(get_session),
    token_data: dict = Depends(verify_jwt_token)
):
    """
    Perform a stateless handshake to initialize conversation context
    """
    try:
        # Validate that the user_id in the request matches the authenticated user
        user_id = token_data.get("user_id")

        handshake_tool = get_chat_handshake_mcp_tool()
        result = await handshake_tool.execute(
            session_id=request.session_id,
            user_id=user_id,
            #context_size=10
        )

        return result
    except HTTPException:
        raise  # Re-raise HTTP exceptions as-is
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Handshake failed: {str(e)}")