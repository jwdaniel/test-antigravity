# Implementation Plan - Modular FastAPI with Dockerized PostgreSQL

## Goal Description
Initialize a minimized, modularized FastAPI project using `uv` for dependency management. The project will use PostgreSQL 16 via Docker and target Python 3.12+. It will include a basic structure with database integration and testing setup to achieve at least 68% code coverage.

## User Review Required
- **Project Location**: I will create a subdirectory `fastapi-uv-project` to avoid cluttering the root workspace.
- **Dependencies**: Using `fastapi`, `uvicorn`, `sqlalchemy`, `asyncpg`, `pydantic-settings`.

## Proposed Changes

### Project Root
#### [NEW] `fastapi-uv-project/`
- `pyproject.toml`: Dependency management.
- `docker-compose.yml`: PostgreSQL service.
- `.env`: Environment variables.
- `Dockerfile`: For the application (optional, but good for "dockerised" context, though user asked for dockerised Postgres specifically). *Self-correction: User said "dockerised PostgreSQL", implying the app runs locally or in docker. I will provide a Dockerfile for the app too as best practice.*

### Application Code (`app/`)
#### [NEW] `app/main.py`
- Entry point, FastAPI app initialization.
#### [NEW] `app/core/config.py`
- Settings management using `pydantic-settings`.
#### [NEW] `app/db/session.py`
- SQLAlchemy async engine and session maker.
#### [NEW] `app/api/`
- Modular routers.

### Tests (`tests/`)
#### [NEW] `tests/conftest.py`
- Fixtures for async client and database.
#### [NEW] `tests/test_main.py`
- Health check tests.

## Verification Plan
### Automated Tests
- Run `uv run pytest --cov=app tests/` to check coverage.
### Manual Verification
- Start DB: `docker-compose up -d`
- Run App: `uv run uvicorn app.main:app --reload`
- Check Swagger UI: `http://localhost:8000/docs`
