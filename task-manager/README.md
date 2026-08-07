# Task Manager API

This project is a Kubernetes learning lab that will grow incrementally into a production-quality Task Manager API.

## Current milestone: Milestone 2 — Minimal FastAPI application

Milestone 2 adds a minimal FastAPI application with two status endpoints and Uvicorn-compatible application startup.

## Project structure

```text
task-manager/
├── backend/
│   ├── app/
│   │   └── main.py
│   ├── api/
│   │   └── routes.py
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── database/
│   ├── core/
│   │   ├── config.py
│   │   └── logging.py
│   └── tests/
│       └── test_status.py
├── requirements.txt
└── README.md
```

## Directory purpose

- `backend/`: Contains the Python backend source tree and tests.
- `backend/app/`: Contains the FastAPI application factory and runtime entry point used by Uvicorn.
- `backend/api/`: Contains API routers and endpoint definitions.
- `backend/models/`: Will contain SQLAlchemy ORM models that map Python classes to database tables.
- `backend/schemas/`: Will contain Pydantic schemas for request validation and response serialization.
- `backend/services/`: Will contain business logic separated from HTTP route handlers.
- `backend/database/`: Will contain database engine, session, and migration-related configuration as the project grows.
- `backend/core/`: Contains shared core configuration such as environment settings and logging.
- `backend/tests/`: Contains automated tests for the backend.
- `requirements.txt`: Defines Python package dependencies for local development and, later, Docker image builds.
- `README.md`: Documents the project, milestone status, and learning notes.

## API endpoints

| Method | Path | Response |
| --- | --- | --- |
| `GET` | `/` | `{ "status": "healthy" }` |
| `GET` | `/health` | `{ "status": "ok" }` |

## Running locally

From the `task-manager/backend` directory, run:

```bash
uvicorn app.main:app --reload
```

The application is then available at `http://127.0.0.1:8000`.

## FastAPI startup

Uvicorn imports `app.main:app`. The `app` object is created by `create_app()`, which configures the FastAPI instance and includes the API router. The lifespan handler configures logging at startup and logs shutdown when the server exits.

## Routers

Routes live in `backend/api/routes.py` and are attached to the FastAPI application from `backend/app/main.py`. Keeping routes outside the application factory keeps endpoint definitions organized as the API grows.

## Dependency injection

FastAPI dependency injection is introduced through `Depends(get_settings)`. The settings dependency is cached and reads environment variables with the `TASK_MANAGER_` prefix, which will later map cleanly to Docker and Kubernetes environment variable injection.

## Kubernetes learning path

This milestone still does not include Docker or Kubernetes files. Later, Docker will package this FastAPI application into an image, and Kubernetes will run that image in Pods behind Services and health checks.
