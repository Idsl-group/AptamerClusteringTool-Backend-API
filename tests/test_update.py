import pytest
from httpx import AsyncClient
from e2edna_api.app.main import app


# Test the update endpoint
@pytest.mark.asyncio
async def test_update_endpoint(monkeypatch):
    # Mock the read_yaml and write_yaml functions
    async def mock_read_yaml(path):
        return {
            'mode': 'old_mode',
            'aptamer_seq': 'old_sequence',
            'ligand': 'old_ligand',
            'ligand_type': 'old_ligand_type',
            'ligand_seq': 'old_ligand_seq'
        }

    async def mock_write_yaml(path, data):
        return True

    from e2edna_api.app.config.yaml import read_yaml, write_yaml
    monkeypatch.setattr(read_yaml, "read_yaml", mock_read_yaml)
    monkeypatch.setattr(write_yaml, "write_yaml", mock_write_yaml)

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/update", json={
            "dock_mode": "coarse dock",
            "sequence": "ACTGCCTAACTTAAAATTTTTGGGTGTGAG",
            "ligand": "new_ligand",
            "ligand_type": "new_ligand_type",
            "ligand_seq": "new_ligand_seq"
        })
    assert response.status_code == 200
    assert response.json() == True
