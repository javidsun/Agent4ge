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

## Run

Run as a module:

```bash
python -m agent4ge
```

Run the console command after installing:

```bash
agent4ge
```

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
