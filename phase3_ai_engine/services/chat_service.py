"""
Chat Service - Phase 4 (Hackathon Winner Tier - Autonomous Agent Mode)
"""

import re
import uuid
import sys
import json
import logging
from typing import List, Dict, Any, Tuple
from pathlib import Path
from difflib import SequenceMatcher

from rapidfuzz import fuzz
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select

current_file = Path(__file__).resolve()
phase_root = current_file.parent.parent
if str(phase_root) not in sys.path:
    sys.path.insert(0, str(phase_root))

from models import ChatHistory
from ai_client import get_cohere_client
from mcp_tools.todo_tool import get_todo_mcp_tool

logger = logging.getLogger("todo_chat_agent")
logger.setLevel(logging.INFO)


class ChatService:

    INTENT_CONFIDENCE_THRESHOLD = 0.65

    def __init__(self, session: AsyncSession):
        self.session = session
        self.ai_client = get_cohere_client()
        self.todo_tool = get_todo_mcp_tool()
        self.pending_confirmations = {}

    # ======================================================
    # DATABASE
    # ======================================================

    async def save_message(self, session_id: str, role: str, content: Any):
        try:
            if not isinstance(content, str):
                content = json.dumps(content, default=str)

            message = ChatHistory(
                id=uuid.uuid4(),
                session_id=session_id,
                role=role,
                content=content
            )
            self.session.add(message)
            await self.session.commit()
        except Exception as e:
            logger.error(f"[DB ERROR] {e}")
            await self.session.rollback()

    async def get_recent_messages(self, session_id: str, limit: int = 8):
        statement = (
            select(ChatHistory)
            .where(ChatHistory.session_id == session_id)
            .order_by(ChatHistory.created_at.desc())
            .limit(limit)
        )
        result = await self.session.execute(statement)
        messages = result.scalars().all()

        return [{"role": m.role, "content": m.content} for m in reversed(messages)]

    async def get_user_tasks(self, user_id: str):
        tasks_res = await self.todo_tool.execute(
            operation="list",
            user_id=user_id
        )
        return tasks_res.get("tasks", []) if tasks_res.get("success") else []

    # ======================================================
    # INTENT DETECTION
    # ======================================================

    def detect_intent(self, text: str) -> Tuple[str, float]:
        text_clean = text.lower().strip()

        if text_clean in ["yes", "ok", "confirm", "yup", "sure"]:
            return "confirm", 1.0

        patterns = {
            "create": ["add", "create", "new task", "remember"],
            "delete": ["delete", "remove"],
            "update": ["update", "edit", "change", "modify"],
            "complete": ["complete", "done", "finish"],
            "list": ["show", "list", "view"],
        }

        best_intent = "chat"
        best_score = 0.0

        for intent, keywords in patterns.items():
            for keyword in keywords:
                score = fuzz.partial_ratio(text_clean, keyword) / 100
                if score > best_score:
                    best_score = score
                    best_intent = intent

        return best_intent, best_score

    # ======================================================
    # TASK MATCHING
    # ======================================================

    def similarity_score(self, a: str, b: str):
        return SequenceMatcher(None, a.lower(), b.lower()).ratio()

    def resolve_task_id(self, user_input: str, tasks: List[Dict]):

        if not tasks:
            return None, None, 0

        scored = []
        user_input_lower = user_input.lower().strip()

        for task in tasks:
            title = task["title"].lower()
            description = (task.get("description") or "").lower()

            t_fuzz = fuzz.token_set_ratio(user_input_lower, title)
            t_seq = self.similarity_score(user_input_lower, title) * 100
            t_score = (t_fuzz * 0.8) + (t_seq * 0.2)

            d_fuzz = fuzz.token_set_ratio(user_input_lower, description)
            d_score = d_fuzz

            final_score = max(t_score, d_score)

            if user_input_lower in title or user_input_lower in description:
                final_score = max(final_score, 90)

            scored.append({
                "id": task["id"],
                "title": task["title"],
                "score": final_score
            })

        scored.sort(key=lambda x: x["score"], reverse=True)

        best = scored[0]

        if best["score"] < 50:
            return None, None, best["score"]

        return best["id"], best["title"], best["score"]


    # ======================================================
    # MAIN PROCESSOR
    # ======================================================

    async def process_user_query(self, session_id, user_input, user_id):

        await self.save_message(session_id, "user", user_input)

        intent, confidence = self.detect_intent(user_input)

        if confidence < self.INTENT_CONFIDENCE_THRESHOLD:
            return await self.handle_chat(session_id, user_input)

        if intent == "create":
            return await self.handle_create(session_id, user_input, user_id)

        if intent == "delete":
            return await self.handle_delete(session_id, user_input, user_id)

        if intent == "update":
            return await self.handle_update(session_id, user_input, user_id)

        if intent == "complete":
            return await self.handle_complete(session_id, user_input, user_id)

        if intent == "list":
            return await self.handle_list(session_id, user_id)

        return await self.handle_chat(session_id, user_input)

    # ======================================================
    # ACTIONS
    # ======================================================

    async def handle_create(self, session_id, user_input, user_id):

        title = re.sub(r'^(add|create)\s+', '', user_input, flags=re.I).strip()

        task_data = {
            "title": title.capitalize(),
            "description": title,
            "priority": "medium",
            "due_date": None
        }

        await self.todo_tool.execute(
            operation="create",
            task_data=task_data,
            user_id=user_id
        )

        response = f"🚀 Task '{task_data['title']}' created."

        await self.save_message(session_id, "assistant", response)

        return {"response": response, "refresh_tasks": True, "optimistic": True}

    async def handle_delete(self, session_id, user_input, user_id):

        tasks = await self.get_user_tasks(user_id)
        user_input = re.sub(r'\b(delete|remove)\b', '', user_input, flags=re.I).strip()

        task_id, title, confidence = self.resolve_task_id(user_input, tasks)

        if not task_id:
            return {"response": "Task not found."}

        await self.todo_tool.execute(
            operation="delete",
            task_id=str(task_id),
            user_id=user_id
        )

        response = f"✅ '{title}' deleted."

        await self.save_message(session_id, "assistant", response)

        return {"response": response, "refresh_tasks": True}

    async def handle_update(self, session_id, user_input, user_id):

        tasks = await self.get_user_tasks(user_id)

        if not tasks:
            return {"response": "You have no tasks to update."}

        cleaned = re.sub(r'^(update|edit|change|modify)\s+', '', user_input, flags=re.I)
        parts = re.split(r'\s+to\s+', cleaned, maxsplit=1, flags=re.I)

        if len(parts) != 2:
            return {"response": "Use format: update <task> to <new description>"}

        search_term = parts[0].strip()
        new_desc = parts[1].strip()

        task_id, title, confidence = self.resolve_task_id(search_term, tasks)

        if not task_id:
            return {"response": "Task not found."}

        result = await self.todo_tool.execute(
            operation="update",
            task_id=str(task_id),
            user_id=user_id,
            task_data={
                "description": new_desc
            }
        )

        if not result.get("success"):
            return {"response": "Update failed."}

        response = "✏️ Task updated successfully."

        await self.save_message(session_id, "assistant", response)

        return {
            "response": response,
            "refresh_tasks": True,
            "optimistic": True
        }

    async def handle_complete(self, session_id, user_input, user_id):

        tasks = await self.get_user_tasks(user_id)

        is_negation = any(word in user_input.lower() for word in ["not", "undo", "un", "pending","incomplete"])
        target_status = False if is_negation else True

        search_query = re.sub(r'\b(complete|done|finish|mark|in|is)\b', '', user_input, flags=re.I).strip()

        task_id, title, confidence = self.resolve_task_id(search_query, tasks)

        if not task_id:
            return {"response": "Task not found."}

        await self.todo_tool.execute(
            operation="complete",
            task_id=str(task_id),
            user_id=user_id,
            task_data={"completed": target_status}
        )

        status_msg = "completed ✅" if target_status else "marked pending ↩️"

        response = f"'{title}' {status_msg}."

        await self.save_message(session_id, "assistant", response)

        return {"response": response, "refresh_tasks": True, "optimistic": True}

    async def handle_list(self, session_id, user_id):

        tasks = await self.get_user_tasks(user_id)

        if not tasks:
            return {"response": "No tasks found."}

        formatted = "\n".join(
            f"• {t['title']} ({'Done' if t.get('completed') else 'Pending'})"
            for t in tasks
        )

        response = f"📋 Your Tasks:\n\n{formatted}"

        await self.save_message(session_id, "assistant", response)

        return {"response": response}

    async def handle_chat(self, session_id, user_input):

        recent = await self.get_recent_messages(session_id)

        prompt = f"Conversation:\n{recent}\nUser: {user_input}"

        ai = await self.ai_client.chat_completion(prompt)

        reply = ai.choices[0].message.content

        await self.save_message(session_id, "assistant", reply)

        return {"response": reply}
