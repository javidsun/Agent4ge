from fastapi.testclient import TestClient

from agent4ge.main import app


def test_health_returns_200() -> None:
    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200


def test_health_returns_status_ok() -> None:
    client = TestClient(app)

    response = client.get("/health")

    assert response.json() == {"status": "ok"}
