import pytest
from httpx import AsyncClient
from app.core.config import settings

@pytest.mark.asyncio
async def test_create_item(client: AsyncClient):
    response = await client.post(
        f"{settings.API_V1_STR}/items/",
        json={"title": "Test Item", "description": "A test item"}
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == "Test Item"
    assert content["description"] == "A test item"
    assert "id" in content

@pytest.mark.asyncio
async def test_read_items(client: AsyncClient):
    response = await client.get(f"{settings.API_V1_STR}/items/")
    assert response.status_code == 200
    content = response.json()
    assert isinstance(content, list)
