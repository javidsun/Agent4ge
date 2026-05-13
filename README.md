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

## Configuration

Local configuration is managed through environment variables. Create a local
`.env` file from the example file:

```bash
cp .env.example .env
```

Supported variables:

- `APP_ENV`: application environment, defaults to `local`
- `DATABASE_URL`: database connection URL, empty by default
- `API_PREFIX`: API route prefix, defaults to `/api/v1`
- `LOG_LEVEL`: application log level, defaults to `INFO`

The `.env` file is for local configuration and must not be committed.

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
├── .env.example
├── src/
│   └── agent4ge/
│       ├── __init__.py
│       ├── __main__.py
│       ├── config.py
│       └── main.py
└── tests/
    ├── test_config.py
    └── test_smoke.py
```
