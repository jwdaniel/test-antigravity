# Modular FastAPI with Dockerized PostgreSQL

A minimized, modularized FastAPI project using `uv` and Docker, designed for gradual feature development.

## Features
- **Dependency Management**: Uses `uv` for fast and reliable dependency management.
- **Database**: PostgreSQL 16 running in Docker.
- **ORM**: SQLAlchemy (Async) with `asyncpg`.
- **Migrations**: Alembic for database schema management.
- **Configuration**: `pydantic-settings` for environment-based config.
- **Testing**: `pytest` with `httpx` and `pytest-cov`.
- **Documentation**: Integrated `docs/` folder for roadmap and planning.

## Project Structure
```
fastapi-uv-project/
├── app/
│   ├── api/v1/          # API Routers
│   ├── core/            # Configuration
│   ├── db/              # Database session & base models
│   ├── models/          # SQLAlchemy models
│   ├── schemas/         # Pydantic schemas
│   └── main.py          # Entry point
├── docs/
│   ├── planning/        # Design documents
│   └── ROADMAP.md       # Project status
├── migrations/          # Alembic migrations
├── tests/               # Tests
├── docker-compose.yml   # Docker services
├── pyproject.toml       # Dependencies
├── alembic.ini          # Alembic config
└── .env                 # Environment variables
```

## How to Run

### Prerequisites
- Python 3.12+
- `uv` (Universal Python Package Manager)
- Docker & Docker Compose

### Steps
1. **Start Database**:
   ```bash
   docker-compose up -d
   ```

2. **Install Dependencies**:
   ```bash
   uv sync
   ```

3. **Run Migrations**:
   ```bash
   uv run alembic upgrade head
   ```

4. **Run Application**:
   ```bash
   uv run uvicorn app.main:app --reload
   ```
   Access the API docs at http://localhost:8000/docs

5. **Run Tests**:
   ```bash
   uv run python -m pytest --cov=app tests/
   ```

## Development Workflow
- **Planning**: Check `docs/ROADMAP.md` for status and `docs/planning/` for design docs.
- **Database Changes**: Modify models in `app/models/`, then run:
  ```bash
  uv run alembic revision --autogenerate -m "Description of change"
  uv run alembic upgrade head
  ```
