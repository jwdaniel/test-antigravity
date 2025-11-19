# Implementation Plan - Agentic Layer with Google ADK

## Goal Description
Implement an extensible agentic layer using the **Google Agent Development Kit (ADK)**. The agent will be capable of analyzing data from the database (PostgreSQL) and answering user queries. It will support both **Google Gemini** and **OpenAI** models, configurable via environment variables.

## User Review Required
- **Library**: Using `google-adk` (pending verification of exact package name/availability, fallback to `google-genai` if ADK is a private/preview artifact).
- **LLM Support**: OpenAI and Gemini.
- **Prompts**: Stored as text/YAML files in `app/agent/prompts/`.

## Proposed Changes

### Dependencies
- Add `google-adk` (or equivalent Google Agent library).
- Add `google-genai` (for Gemini).
- Add `openai` (for OpenAI).

### Configuration (`.env` & `config.py`)
- Add `LLM_PROVIDER` (default: `gemini`).
- Add `GEMINI_API_KEY`.
- Add `OPENAI_API_KEY`.

### Agent Architecture (`app/agent/`)
#### [NEW] `app/agent/prompts/`
- Directory for storing prompt templates.
- `analysis_prompt.yaml`: System prompt for data analysis.

#### [NEW] `app/agent/core.py`
- `AgentManager`: Class to initialize the agent with the selected provider.
- Integration with Google ADK's `Agent` class.

#### [NEW] `app/agent/tools.py`
- `db_analysis_tool`: A tool that queries the `items` table and returns summary statistics.

#### [NEW] `app/api/v1/endpoints/agent.py`
- `POST /query`: Endpoint to send user queries to the agent.

### Database Integration
- The agent will use `app.db.session` to execute read-only queries for analysis.

## Verification Plan
### Automated Tests
- Mock LLM responses to test agent logic.
- Test prompt loading mechanism.
- Test tool execution.

### Manual Verification
- Configure `.env` with Gemini Key.
- Run `POST /api/v1/agent/query` with "How many items do we have?".
- Verify the agent queries the DB and returns the count.
- Switch `.env` to OpenAI and repeat.
