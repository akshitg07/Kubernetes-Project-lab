"""Tests for task CRUD endpoints."""

from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from database.base import Base
from database.session import get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}, poolclass=StaticPool
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(name="client")
def client_fixture() -> Generator[TestClient, None, None]:
    Base.metadata.create_all(bind=engine)

    def override_get_db() -> Generator[Session, None, None]:
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as client:
        yield client
    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=engine)


def test_task_crud_flow(client: TestClient) -> None:
    create_response = client.post(
        "/tasks",
        json={"title": "Learn Kubernetes", "description": "Start with FastAPI", "completed": False},
    )
    assert create_response.status_code == 201
    created_task = create_response.json()
    assert created_task["title"] == "Learn Kubernetes"
    assert created_task["completed"] is False

    task_id = created_task["id"]

    list_response = client.get("/tasks")
    assert list_response.status_code == 200
    assert len(list_response.json()) == 1

    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 200
    assert get_response.json()["id"] == task_id

    update_response = client.put(
        f"/tasks/{task_id}",
        json={"title": "Learn Kubernetes deeply", "description": "CRUD first", "completed": True},
    )
    assert update_response.status_code == 200
    updated_task = update_response.json()
    assert updated_task["title"] == "Learn Kubernetes deeply"
    assert updated_task["completed"] is True

    delete_response = client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code == 204

    missing_response = client.get(f"/tasks/{task_id}")
    assert missing_response.status_code == 404
