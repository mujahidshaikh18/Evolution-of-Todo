from fastapi.testclient import TestClient
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the main app
from main import app

# Create test client
client = TestClient(app)

print("Testing auth endpoints...")
response = client.post("/auth/register",
                      json={"email": "test@example.com", "password": "password123", "name": "Test User"})
print(f"Register response: {response.status_code}")
print(f"Register content: {response.text}")

print("\nTesting health endpoint...")
response = client.get("/health")
print(f"Health response: {response.status_code}")
print(f"Health content: {response.text}")

print("\nAll app routes:")
for route in app.routes:
    if hasattr(route, 'path'):
        print(f"  {route.path}")