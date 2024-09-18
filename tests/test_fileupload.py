# test_file_upload.py
import os
import pytest
from fastapi.testclient import TestClient
from ...app.main import app

client = TestClient(app)


# Setup and teardown for the test
@pytest.fixture(scope="module", autouse=True)
def setup_and_teardown():
    # Setup: Create the upload directory if it doesn't exist
    upload_dir = os.path.join(os.getcwd(), "data/test_user")
    os.makedirs(upload_dir, exist_ok=True)
    yield
    # Teardown: Remove the uploaded files after tests
    for file in os.listdir(upload_dir):
        file_path = os.path.join(upload_dir, file)
        if os.path.isfile(file_path):
            os.unlink(file_path)


def test_upload_file():
    file_path = "test_file.txt"
    with open(file_path, "w") as f:
        f.write("This is a test file.")

    with open(file_path, "rb") as f:
        response = client.post(
            "/uploadFile/",
            files={"file": ("test_file.txt", f, "text/plain")},
            data={"user_id": "test_user"}
        )

    assert response.status_code == 200
    response_data = response.json()
    assert response_data["file_name"] == "test_file.txt"
    assert response_data["user_id"] == "test_user"
    assert response_data["status"] is True
    assert response_data["message"] == "File uploaded successfully"

    # Clean up the test file
    os.remove(file_path)
