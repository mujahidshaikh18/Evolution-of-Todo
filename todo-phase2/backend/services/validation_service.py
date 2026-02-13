"""
Validation service for checking task validity and conflicts
"""
from typing import Dict, Any, List, Optional
from sqlmodel import Session, select
from models import Task
from db import get_engine
import re
from datetime import datetime


class ValidationService:
    def __init__(self):
        self.engine = get_engine()

    def check_task_validity(self, task_data: Dict[str, Any], user_id: str) -> Dict[str, Any]:
        """
        Check if a task is valid according to business rules

        Args:
            task_data: Task data to validate
            user_id: User ID for scoping validation

        Returns:
            Dictionary with validation results
        """
        results = {
            "valid": True,
            "errors": [],
            "warnings": [],
            "suggestions": []
        }

        # Check title length
        title = task_data.get('title', '').strip()
        if not title:
            results["valid"] = False
            results["errors"].append("Task title is required")
        elif len(title) < 3:
            results["valid"] = False
            results["errors"].append("Task title is too short (less than 3 characters)")
            results["suggestions"].append("Provide a more descriptive title")

        # Check for duplicates
        duplicate_check = self.check_for_duplicates(task_data, user_id)
        if duplicate_check["has_duplicates"]:
            results["valid"] = False
            results["errors"].extend([dup["title"] for dup in duplicate_check["duplicates"]])
            results["suggestions"].append("Consider modifying the title to differentiate from existing tasks")

        # Check for deadline conflicts
        deadline_check = self.check_for_deadline_conflicts(task_data, user_id)
        if deadline_check["has_conflicts"]:
            results["warnings"].extend([conf["title"] for conf in deadline_check["conflicts"]])
            results["suggestions"].append("Consider adjusting deadlines to avoid conflicts")

        return results

    def check_for_duplicates(self, task_data: Dict[str, Any], user_id: str) -> Dict[str, Any]:
        """
        Check for duplicate task titles

        Args:
            task_data: Task data to check for duplicates
            user_id: User ID for scoping validation

        Returns:
            Dictionary with duplicate check results
        """
        with Session(self.engine) as session:
            title = task_data.get('title', '').strip().lower()
            if not title:
                return {
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
                "has_duplicates": len(similar_tasks) > 0,
                "duplicates": similar_tasks,
                "message": f"Found {len(similar_tasks)} similar task(s)" if similar_tasks else "No duplicates found"
            }

    def check_for_deadline_conflicts(self, task_data: Dict[str, Any], user_id: str) -> Dict[str, Any]:
        """
        Check for deadline conflicts with existing tasks

        Args:
            task_data: Task data to check for deadline conflicts
            user_id: User ID for scoping validation

        Returns:
            Dictionary with deadline conflict results
        """
        with Session(self.engine) as session:
            deadline_str = task_data.get('deadline') or task_data.get('due_date')
            if not deadline_str:
                return {
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
                    "has_conflicts": len(conflicts) > 0,
                    "conflicts": conflicts,
                    "message": f"Found {len(conflicts)} deadline conflict(s)" if conflicts else "No deadline conflicts found"
                }
            except ValueError:
                return {
                    "has_conflicts": False,
                    "conflicts": [],
                    "error": f"Invalid deadline format: {deadline_str}",
                    "message": f"Invalid deadline format: {deadline_str}"
                }

    def _is_similar_title(self, title1: str, title2: str) -> bool:
        """
        Check if two titles are similar (allowing for minor differences)
        """
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


# Global instance
validation_service = ValidationService()


def get_validation_service():
    """Get the global validation service instance"""
    return validation_service