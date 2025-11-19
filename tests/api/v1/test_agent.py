import pytest
from unittest.mock import AsyncMock, patch, MagicMock
from sqlalchemy import text
from app.agent.core import AgentManager

@pytest.mark.asyncio
async def test_agent_manager_gemini_mock():
    with patch("app.agent.core.settings") as mock_settings:
        mock_settings.LLM_PROVIDER = "gemini"
        mock_settings.GEMINI_API_KEY = "fake-key"
        
        with patch("google.genai.Client") as MockClient:
            mock_client_instance = MockClient.return_value
            mock_response = MagicMock()
            mock_response.text = "Gemini response"
            mock_client_instance.models.generate_content.return_value = mock_response
            
            manager = AgentManager()
            response = await manager.process_query("Hello")
            assert response == "Gemini response"

@pytest.mark.asyncio
async def test_agent_manager_openai_mock():
    with patch("app.agent.core.settings") as mock_settings:
        mock_settings.LLM_PROVIDER = "openai"
        mock_settings.OPENAI_API_KEY = "fake-key"
        
        with patch("openai.AsyncOpenAI") as MockClient:
            mock_client_instance = MockClient.return_value
            mock_response = MagicMock()
            mock_response.choices = [MagicMock(message=MagicMock(content="OpenAI response"))]
            mock_client_instance.chat.completions.create = AsyncMock(return_value=mock_response)
            
            manager = AgentManager()
            response = await manager.process_query("Hello")
            assert response == "OpenAI response"

@pytest.mark.asyncio
async def test_agent_tool_execution(db_session):
    # This test verifies the tool logic itself against the DB
    from app.agent.tools import db_analysis_tool
    
    # Clear items to ensure clean state
    await db_session.execute(text("DELETE FROM items"))
    await db_session.commit()

    # Create a dummy item
    from app.models.item import Item
    item = Item(title="Test Item", description="Desc")
    db_session.add(item)
    await db_session.commit()
    
    result = await db_analysis_tool("SELECT COUNT(*) FROM items")
    assert "1" in result
