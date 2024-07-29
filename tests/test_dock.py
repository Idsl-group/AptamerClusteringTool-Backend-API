import pytest
from httpx import AsyncClient
from e2edna_api.app.main import app


# Test the dock endpoint
@pytest.mark.asyncio
async def test_dock_endpoint(monkeypatch):
    # Mock the run_command function
    async def mock_run_command():
        return True

    from e2edna_api.app.api.dock import run_command
    monkeypatch.setattr(run_command, "run_command", mock_run_command)

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/dock", json={
            "attribute1": "value1",
            "attribute2": "value2"
        })
    assert response.status_code == 200
    assert response.json() == {'Executed': True}
