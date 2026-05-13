from fastapi import FastAPI

from agent4ge.config import get_settings

app = FastAPI(title="agent4ge", version="0.1.0")
app.state.settings = get_settings()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
