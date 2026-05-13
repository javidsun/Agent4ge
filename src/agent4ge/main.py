from fastapi import FastAPI

app = FastAPI(title="agent4ge", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
