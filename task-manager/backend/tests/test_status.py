"""Tests for status endpoints."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_returns_healthy_status() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_health_returns_ok_status() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
