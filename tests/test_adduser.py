# test_add_user.py
import pytest
from fastapi.testclient import TestClient
from ...app.main import app  # Adjust the import based on your project structure

client = TestClient(app)

def test_create_user():
    request_data = {
        "username": "test_user",
        "user_id": "test_user_id"
    }

    response = client.post("/addNewUser", json=request_data)

    assert response.status_code == 200
    response_data = response.json()
    assert response_data["user_id"] == "test_user_id"
    assert response_data["status"] is True
    assert response_data["message"] == "User added successfully"