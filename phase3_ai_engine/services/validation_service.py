"""
Validation service for conversation context formatting
"""
from typing import Dict, Any, List
from datetime import datetime


class ValidationService:
    def __init__(self):
        pass

    def format_conversation_context(self, messages: List[Dict[str, Any]]) -> str:
        """
        Format conversation messages into a structured context string

        Args:
            messages: List of message dictionaries with role and content

        Returns:
            Formatted context string
        """
        formatted_context = ""
        for msg in messages:
            role = msg.get('role', 'unknown')
            content = msg.get('content', '')
            timestamp = msg.get('created_at', datetime.utcnow().isoformat())

            formatted_context += f"[{timestamp}] {role.upper()}: {content}\n"

        return formatted_context.strip()

    def validate_conversation_flow(self, messages: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Validate the flow and coherence of a conversation

        Args:
            messages: List of message dictionaries

        Returns:
            Validation results with any issues found
        """
        validation_result = {
            "valid": True,
            "issues": [],
            "suggestions": []
        }

        # Check if there are alternating user/assistant messages
        roles = [msg.get('role', '') for msg in messages]
        for i in range(len(roles) - 1):
            if roles[i] == roles[i+1]:
                validation_result["valid"] = False
                validation_result["issues"].append(f"Consecutive {roles[i]} messages found at position {i}-{i+1}")

        # Check for message content validity
        for i, msg in enumerate(messages):
            content = msg.get('content', '').strip()
            if not content:
                validation_result["valid"] = False
                validation_result["issues"].append(f"Empty message content at position {i}")

        return validation_result


# Global instance
validation_service = ValidationService()


def get_validation_service():
    """Get the global validation service instance"""
    return validation_service