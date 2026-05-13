# agent4ge

A local AI-agent orchestration project for managing coding tasks.

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project with development dependencies:

```bash
pip install -e ".[dev]"
```

## Run Backend

Start the backend with reload enabled:

```bash
uvicorn agent4ge.main:app --reload
```

Or start it through the package module:

```bash
python -m agent4ge
```

OpenAPI documentation is available through FastAPI defaults:

- Health check: http://127.0.0.1:8000/health
- Swagger UI: http://127.0.0.1:8000/docs
- OpenAPI JSON: http://127.0.0.1:8000/openapi.json

## Test

```bash
pytest
```

## Lint

```bash
ruff check .
```

## Folder Structure

```text
.
├── pyproject.toml
├── README.md
├── src/
│   └── agent4ge/
│       ├── __init__.py
│       ├── __main__.py
│       └── main.py
└── tests/
    └── test_smoke.py
```
