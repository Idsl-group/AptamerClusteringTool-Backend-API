# test_file_upload.py
import os
import pytest
from fastapi.testclient import TestClient
from ...app.main import app  # Adjust the import based on your project structure

client = TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def setup_and_teardown():
    # Setup: Create the upload directory if it doesn't exist
    upload_dir = os.path.join(os.getcwd(), "data/test_user")
    os.makedirs(upload_dir, exist_ok=True)
    # Create a test file
    with open(os.path.join(upload_dir, "test_file.txt"), "w") as f:
        f.write("This is a test file.")
    yield
    # Teardown: Remove the uploaded files after tests
    for file in os.listdir(upload_dir):
        file_path = os.path.join(upload_dir, file)
        if os.path.isfile(file_path):
            os.unlink(file_path)

def test_list_files():
    response = client.get("/listFiles/", params={"user_id": "test_user"})
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["user_id"] == "test_user"
    assert "test_file.txt" in response_data["files"]
    assert response_data["status"] is True
    assert response_data["message"] == "Files listed successfully"