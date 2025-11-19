from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.agent.core import agent_manager

router = APIRouter()

class AgentQuery(BaseModel):
    query: str

class AgentResponse(BaseModel):
    response: str

@router.post("/query", response_model=AgentResponse)
async def query_agent(query_request: AgentQuery):
    """
    Send a query to the AI agent.
    """
    try:
        response_text = await agent_manager.process_query(query_request.query)
        return AgentResponse(response=response_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
