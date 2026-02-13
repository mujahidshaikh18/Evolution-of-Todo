import os
import cohere
import asyncio
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Native Cohere V2 Client
# This avoids the "405 Method Not Allowed" error caused by the OpenAI SDK
co = cohere.AsyncClientV2(api_key=os.getenv("COHERE_API_KEY"))

class CohereClient:
    def __init__(self):
        self.client = co
        # Use a stable model slug (e.g., command-r-08-2024) from .env
        self.model = os.getenv("COHERE_MODEL", "command-r-08-2024")

    async def chat_completion(self, messages, temperature=0.7, max_tokens=1000, tools=None):
        """
        Calls Cohere Native V2 API and wraps the response to match OpenAI's format.
        This ensures compatibility with your existing Agent/Runner logic.
        """
        try:
            # Process messages to handle system message for Cohere
            if isinstance(messages, str):
                messages = [{"role": "user", "content": messages}]

            processed_messages = []

            for msg in messages:
                # Basic safety check: ensure msg is a dictionary before calling .get()
                if not isinstance(msg, dict):
                    processed_messages.append({"role": "user", "content": str(msg)})
                    continue
                # Handle different message roles for Cohere V2
                if msg.get("role") == "system":
                    processed_messages.append({"role": "system", "content": msg.get("content", "")})
                elif msg.get("role") == "user":
                    processed_messages.append({"role": "user", "content": msg.get("content", "")})
                elif msg.get("role") == "assistant":
                    # Handle assistant messages that may contain tool_calls
                    assistant_msg = {"role": "assistant", "content": msg.get("content", "")}
                    if "tool_calls" in msg:
                        assistant_msg["tool_calls"] = msg["tool_calls"]
                    processed_messages.append(assistant_msg)
                elif msg.get("role") == "tool":
                    # Format tool results for Cohere V2
                    processed_messages.append({
                        "role": "tool", 
                        "content": msg.get("content", ""),
                        "tool_call_id": msg.get("tool_call_id", "")
                    })
                else:
                    # Default to user role for unrecognized roles
                    processed_messages.append({"role": "user", "content": str(msg)})

            # Prepare the chat call with tools if provided
            chat_params = {
                "model": self.model,
                "messages": processed_messages,
                "temperature": temperature,
                "max_tokens": max_tokens
            }

            # Add tools parameter if tools are provided
            if tools:
                # Convert tools to Cohere V2 format
                cohere_tools = []
                for tool in tools:
                    # Determine required parameters - only include those marked as required
                    required_params = []
                    for param_name, param_details in tool["parameters"].items():
                        # Check if this parameter is required based on description containing "(required)"
                        if "(required)" in param_details.get("description", "").lower():
                            required_params.append(param_name)
                    
                    cohere_tool = {
                        "type": "function",
                        "function": {
                            "name": tool["name"],
                            "description": tool["description"],
                            "parameters": {
                                "type": "object",
                                "properties": tool["parameters"],
                                "required": required_params
                            }
                        }
                    }
                    cohere_tools.append(cohere_tool)

                chat_params["tools"] = cohere_tools

            # Direct Async V2 Chat Call - this is now properly async
            response = await self.client.chat(**chat_params)

            # Check if there are tool calls in the response
            if hasattr(response.message, 'tool_calls') and response.message.tool_calls and len(response.message.tool_calls) > 0:
                # Process tool calls and get results
                tool_results = []

                # Return a structured response indicating tool calls were detected
                # The service layer will handle the actual execution and follow-up call
                tool_calls_info = []
                for tool_call in response.message.tool_calls:
                    # Parse the arguments JSON string
                    import json
                    try:
                        arguments = json.loads(tool_call.function.arguments)
                    except:
                        arguments = {}  # Default to empty if parsing fails

                    tool_calls_info.append({
                        "id": tool_call.id,  # Capture the exact ID from the AI
                        "function": {
                            "name": tool_call.function.name,
                            "arguments": arguments  # Parsed arguments
                        },
                        "type": "function"
                    })

                # Return a structured response indicating tool calls were detected
                # This allows the service layer to handle the actual execution
                content_text = f"TOOL_CALLS_DETECTED:" + str(tool_calls_info)
            else:
                # Extract content from Cohere V2 response (Nested in message.content[0].text)
                # This is the final response text after tool execution
                content_text = response.message.content[0].text

            # Mock the OpenAI Response structure
            # Your ChatService/Runner expects response.choices[0].message.content
            class MockMessage:
                def __init__(self, content):
                    self.content = content
                    self.role = "assistant"

            class MockChoice:
                def __init__(self, content):
                    self.message = MockMessage(content)

            class MockResponse:
                def __init__(self, content):
                    self.choices = [MockChoice(content)]

            return MockResponse(content_text)

        except Exception as e:
            print(f"--- COHERE NATIVE V2 DEBUG START ---")
            print(f"Error: {str(e)}")
            print(f"--- COHERE NATIVE V2 DEBUG END ---")
            raise

# Global instance for the application
cohere_client = CohereClient()

def get_cohere_client():
    """Returns the global Cohere client instance"""
    return cohere_client