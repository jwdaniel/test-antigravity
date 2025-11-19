import pytest
import os
from app.agent.core import AgentManager
from app.core.config import settings

# Skip these tests if API keys are not set or if explicitly skipped
run_e2e = pytest.mark.skipif(
    os.getenv("RUN_E2E") != "true",
    reason="Skipping E2E tests. Set RUN_E2E=true to run."
)

@run_e2e
@pytest.mark.asyncio
async def test_agent_e2e_gemini_real_call():
    """
    This test makes a REAL call to Google Gemini.
    Requires GEMINI_API_KEY to be set in .env
    """
    if not settings.GEMINI_API_KEY or "your-gemini-api-key" in settings.GEMINI_API_KEY:
        pytest.skip("GEMINI_API_KEY not set")

    # Temporarily force provider to Gemini
    original_provider = settings.LLM_PROVIDER
    settings.LLM_PROVIDER = "gemini"
    
    try:
        manager = AgentManager()
        # Ask a simple question that doesn't require DB tools to avoid setup complexity in E2E
        response = await manager.process_query("Say 'Hello E2E' and nothing else.")
        assert "Hello E2E" in response
    finally:
        settings.LLM_PROVIDER = original_provider

@run_e2e
@pytest.mark.asyncio
async def test_agent_e2e_openai_real_call():
    """
    This test makes a REAL call to OpenAI.
    Requires OPENAI_API_KEY to be set in .env
    """
    if not settings.OPENAI_API_KEY or "your-openai-api-key" in settings.OPENAI_API_KEY:
        pytest.skip("OPENAI_API_KEY not set")

    # Temporarily force provider to OpenAI
    original_provider = settings.LLM_PROVIDER
    settings.LLM_PROVIDER = "openai"
    
    try:
        manager = AgentManager()
        response = await manager.process_query("Say 'Hello E2E' and nothing else.")
        assert "Hello E2E" in response
    finally:
        settings.LLM_PROVIDER = original_provider
