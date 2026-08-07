# Task Manager API

This project is a Kubernetes learning lab that will grow incrementally into a production-quality Task Manager API.

## Current milestone: Milestone 1 — Project skeleton

Milestone 1 creates the initial project layout only. It intentionally does not include application code, Docker files, or Kubernetes manifests yet.

## Project structure

```text
task-manager/
├── backend/
│   ├── app/
│   ├── api/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── database/
│   ├── core/
│   └── tests/
├── requirements.txt
└── README.md
```

## Directory purpose

- `backend/`: Contains the Python backend source tree and tests.
- `backend/app/`: Will contain the FastAPI application factory and runtime entry points.
- `backend/api/`: Will contain API routers and endpoint definitions.
- `backend/models/`: Will contain SQLAlchemy ORM models that map Python classes to database tables.
- `backend/schemas/`: Will contain Pydantic schemas for request validation and response serialization.
- `backend/services/`: Will contain business logic separated from HTTP route handlers.
- `backend/database/`: Will contain database engine, session, and migration-related configuration as the project grows.
- `backend/core/`: Will contain shared core configuration such as environment settings and logging.
- `backend/tests/`: Will contain automated tests for the backend.
- `requirements.txt`: Defines Python package dependencies for local development and, later, Docker image builds.
- `README.md`: Documents the project, milestone status, and learning notes.

## Kubernetes learning path

This skeleton is intentionally simple. Later milestones will add the FastAPI application, persistence, Docker packaging, Kubernetes manifests, Helm, CI/CD, and observability step by step.
