#!/usr/bin/env python3
"""
Main entry point for the MCP Server
"""
import asyncio
import argparse
from .mcp_server import get_mcp_server


def main():
    parser = argparse.ArgumentParser(description="MCP Server for AI-Powered Todo Chatbot")
    parser.add_argument("--host", type=str, default="localhost", help="Host to bind the server to")
    parser.add_argument("--port", type=int, default=8001, help="Port to bind the server to")

    args = parser.parse_args()

    print("Starting MCP Server for AI-Powered Todo Chatbot...")
    print(f"Listening on {args.host}:{args.port}")

    # Get the MCP server instance
    server = get_mcp_server()

    # Start the server
    server.start(host=args.host, port=args.port)


if __name__ == "__main__":
    main()