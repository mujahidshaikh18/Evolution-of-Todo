"""
Basic tests for the Todo API backend
"""

import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture
def client():
    """Create a test client for the API"""
    return TestClient(app)

def test_health_endpoint(client):
    """Test that the health endpoint works"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_api_routes_exist(client):
    """Test that API routes return appropriate responses (without authentication)"""
    # Test that we get a 401 for unauthorized access rather than 404
    # This confirms the routes exist but require authentication
    response = client.get("/api/test/tasks")
    # This would typically return 401/403 due to auth requirements
    assert response.status_code in [401, 403, 422]  # 422 if invalid user_id format

if __name__ == "__main__":
    pytest.main([__file__])