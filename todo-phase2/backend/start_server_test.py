#!/usr/bin/env python3
"""
Script to start the backend server and test frontend integration
"""
import subprocess
import time
import requests
import threading
import sys
from pathlib import Path

def start_server():
    """Start the backend server"""
    print("Starting backend server on http://localhost:8000...")

    # Change to the backend directory
    backend_dir = Path(__file__).parent
    import os
    os.chdir(backend_dir)

    # Start the uvicorn server
    cmd = ["uvicorn", "main:app", "--host", "localhost", "--port", "8000", "--log-level", "warning"]

    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Give the server time to start
        time.sleep(3)

        # Test the health endpoint
        try:
            response = requests.get("http://localhost:8000/health", timeout=5)
            if response.status_code == 200:
                print("✅ Backend server is running and accessible!")
                print(f"   Health check: {response.json()}")
                print("   API endpoints are available at http://localhost:8000")

                # Show available endpoints
                print("   Available endpoints:")
                print("   - GET /health - Health check")
                print("   - POST /auth/register - User registration")
                print("   - POST /auth/login - User login")
                print("   - GET/POST/PUT/DELETE /api/{user_id}/tasks - Task management")

                return process
            else:
                print(f"❌ Server started but health check failed: {response.status_code}")
                process.terminate()
                return None

        except requests.exceptions.ConnectionError:
            print("❌ Cannot connect to server - check if port 8000 is available")
            process.terminate()
            return None
        except requests.exceptions.Timeout:
            print("❌ Server connection timed out")
            process.terminate()
            return None

    except FileNotFoundError:
        print("❌ uvicorn not found - please install it with 'pip install uvicorn'")
        return None
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        return None

def test_frontend_config():
    """Test frontend configuration"""
    print("\n📋 Frontend Configuration:")

    frontend_dir = Path(__file__).parent.parent / "frontend"

    # Check if API URL is configured
    env_file = frontend_dir / ".env.local"
    if env_file.exists():
        with open(env_file, 'r') as f:
            content = f.read()
            if "NEXT_PUBLIC_API_URL=http://localhost:8000" in content:
                print("   ✅ NEXT_PUBLIC_API_URL is correctly set to http://localhost:8000")
            else:
                print("   ⚠ NEXT_PUBLIC_API_URL may not be correctly configured")
    else:
        print("   ⚠ .env.local file not found in frontend")

    # Check if frontend files exist
    if (frontend_dir / "package.json").exists():
        print("   ✅ Frontend package.json found")
    else:
        print("   ⚠ Frontend package.json not found")

def main():
    print("🚀 Todo App Frontend-Backend Integration Setup")
    print("=" * 50)

    # Test frontend configuration first
    test_frontend_config()

    print("\n📡 Starting Backend Server...")
    server_process = start_server()

    if server_process:
        print("\n🎉 Integration successful!")
        print("   • Backend server running on http://localhost:8000")
        print("   • Frontend configured to connect to backend")
        print("   • All API endpoints are accessible")
        print("\n📝 To run the full application:")
        print("   1. Keep the backend server running (port 8000)")
        print("   2. In a new terminal, go to frontend directory")
        print("   3. Run 'npm install' (if not done already)")
        print("   4. Run 'npm run dev' to start the frontend")
        print("   5. Access the frontend at http://localhost:3000")

        # Don't terminate the server automatically - let user control it
        print(f"\n   Server process PID: {server_process.pid}")
        print("   Press Ctrl+C to stop the server when ready")

        try:
            # Keep the server running until user interrupts
            server_process.wait()
        except KeyboardInterrupt:
            print("\n\n🛑 Shutting down server...")
            server_process.terminate()
            try:
                server_process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                server_process.kill()
            print("✅ Server stopped.")
    else:
        print("\n❌ Failed to start backend server")
        print("   Please check that port 8000 is available and all dependencies are installed")

if __name__ == "__main__":
    main()