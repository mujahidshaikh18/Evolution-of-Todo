"""
MCP Tool for proactive guard functionality (duplicate detection, deadline validation)
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
from models import Task
from db import get_engine
from services.validation_service import get_validation_service
import re


class ProactiveGuardMCPTask:
    def __init__(self):
        self.engine = get_engine()
        self.validation_service = get_validation_service()

    def execute(self, operation: str, task_data: Optional[Dict[str, Any]] = None, user_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Execute proactive guard operations

        Args:
            operation: Operation to perform (check_duplicates, check_deadlines, validate)
            task_data: Task details to validate
            user_id: User ID for scoping validation

        Returns:
            Dictionary with validation results and suggestions
        """
        with Session(self.engine) as session:
            try:
                if operation == "check_duplicates":
                    return self._check_duplicates(session, task_data, user_id)
                elif operation == "check_deadlines":
                    return self._check_deadlines(session, task_data, user_id)
                elif operation == "validate":
                    return self._validate_task(session, task_data, user_id)
                else:
                    raise ValueError(f"Unsupported operation: {operation}")
            except Exception as e:
                return {
                    "success": False,
                    "error": str(e),
                    "operation": operation
                }

    def _check_duplicates(self, session: Session, task_data: Optional[Dict[str, Any]], user_id: Optional[str]) -> Dict[str, Any]:
        """Check for duplicate task titles"""
        if not task_data or not user_id:
            raise ValueError("task_data and user_id are required for duplicate check")

        title = task_data.get('title', '').strip().lower()
        if not title:
            return {
                "success": True,
                "operation": "check_duplicates",
                "has_duplicates": False,
                "duplicates": [],
                "message": "No title provided, no duplicate check performed"
            }

        # Find tasks with similar titles for the user
        statement = select(Task).where(Task.user_id == user_id)
        user_tasks = session.exec(statement).all()

        similar_tasks = []
        for task in user_tasks:
            if task.title.lower() == title or self._is_similar_title(task.title.lower(), title):
                similar_tasks.append({
                    "id": task.id,
                    "title": task.title,
                    "completed": task.completed
                })

        return {
            "success": True,
            "operation": "check_duplicates",
            "has_duplicates": len(similar_tasks) > 0,
            "duplicates": similar_tasks,
            "message": f"Found {len(similar_tasks)} similar task(s)" if similar_tasks else "No duplicates found"
        }

    def _is_similar_title(self, title1: str, title2: str) -> bool:
        """Check if two titles are similar (allowing for minor differences)"""
        # Normalize titles by removing extra whitespace and common variations
        norm1 = re.sub(r'\s+', ' ', title1.strip())
        norm2 = re.sub(r'\s+', ' ', title2.strip())

        # Direct match
        if norm1 == norm2:
            return True

        # Check for common variations (e.g., "buy milk" vs "buy some milk")
        # Remove common words like "some", "a", "an", "the" and compare
        common_words = ['some', 'a', 'an', 'the', 'to', 'be']
        words1 = [word for word in norm1.split() if word not in common_words]
        words2 = [word for word in norm2.split() if word not in common_words]

        # If at least 80% of words match, consider it a duplicate
        if len(words1) > 0 and len(words2) > 0:
            common_count = len(set(words1) & set(words2))
            total_count = max(len(words1), len(words2))
            if total_count > 0 and (common_count / total_count) >= 0.8:
                return True

        return False

    def _check_deadlines(self, session: Session, task_data: Optional[Dict[str, Any]], user_id: Optional[str]) -> Dict[str, Any]:
        """Check for deadline conflicts"""
        if not task_data or not user_id:
            return {
                "success": True,
                "operation": "check_deadlines",
                "has_conflicts": False,
                "conflicts": [],
                "message": "No task data provided, no deadline check performed"
            }

        # This is a placeholder implementation - actual deadline checking would depend on
        # how deadlines are represented in the task data
        # For now, we'll just check if there's a deadline field and validate it

        deadline_str = task_data.get('deadline') or task_data.get('due_date')
        if not deadline_str:
            return {
                "success": True,
                "operation": "check_deadlines",
                "has_conflicts": False,
                "conflicts": [],
                "message": "No deadline specified, no conflict check performed"
            }

        try:
            # Parse the deadline
            deadline = datetime.fromisoformat(deadline_str.replace('Z', '+00:00')) if 'T' in deadline_str else datetime.strptime(deadline_str, '%Y-%m-%d')

            # Find tasks with deadlines in the same timeframe
            statement = select(Task).where(Task.user_id == user_id)
            user_tasks = session.exec(statement).all()

            conflicts = []
            for task in user_tasks:
                task_deadline_str = getattr(task, 'deadline', None) or getattr(task, 'due_date', None)
                if task_deadline_str:
                    try:
                        task_deadline = datetime.fromisoformat(task_deadline_str.replace('Z', '+00:00')) if 'T' in task_deadline_str else datetime.strptime(task_deadline_str, '%Y-%m-%d')

                        # Check if deadlines are within 24 hours of each other (potential conflict)
                        time_diff = abs((deadline - task_deadline).total_seconds())
                        if time_diff <= 24 * 3600:  # 24 hours in seconds
                            conflicts.append({
                                "id": task.id,
                                "title": task.title,
                                "deadline": task_deadline_str,
                                "time_difference_hours": round(time_diff / 3600, 2)
                            })
                    except ValueError:
                        # Skip tasks with invalid deadline format
                        continue

            return {
                "success": True,
                "operation": "check_deadlines",
                "has_conflicts": len(conflicts) > 0,
                "conflicts": conflicts,
                "message": f"Found {len(conflicts)} deadline conflict(s)" if conflicts else "No deadline conflicts found"
            }
        except ValueError:
            return {
                "success": False,
                "operation": "check_deadlines",
                "has_conflicts": False,
                "conflicts": [],
                "error": f"Invalid deadline format: {deadline_str}",
                "message": f"Invalid deadline format: {deadline_str}"
            }

    def _validate_task(self, session: Session, task_data: Optional[Dict[str, Any]], user_id: Optional[str]) -> Dict[str, Any]:
        """Perform comprehensive validation on a task"""
        if not task_data or not user_id:
            raise ValueError("task_data and user_id are required for validation")

        # Use the validation service for comprehensive validation
        validation_result = self.validation_service.check_task_validity(task_data, user_id)

        # Format the result to match MCP tool requirements
        result = {
            "success": True,
            "operation": "validate",
            "valid": validation_result["valid"],
            "warnings": validation_result["warnings"],
            "errors": validation_result["errors"],
            "suggestions": validation_result["suggestions"]
        }

        return result


# Global instance
proactive_guard_mcp_tool = ProactiveGuardMCPTask()


def get_proactive_guard_mcp_tool():
    """Get the global proactive guard MCP tool instance"""
    return proactive_guard_mcp_tool