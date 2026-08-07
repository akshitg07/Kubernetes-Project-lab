# Task Manager API

This project is a Kubernetes learning lab that will grow incrementally into a production-quality Task Manager API.

## Current milestone: Milestone 3 — Task CRUD with SQLite

Milestone 3 adds a real Task resource with create, read, update, delete, and list operations backed by SQLite through SQLAlchemy.

## Project structure

```text
task-manager/
├── backend/
│   ├── app/
│   │   └── main.py
│   ├── api/
│   │   ├── routes.py
│   │   └── tasks.py
│   ├── models/
│   │   └── task.py
│   ├── schemas/
│   │   └── task.py
│   ├── services/
│   │   └── task_service.py
│   ├── database/
│   │   ├── base.py
│   │   └── session.py
│   ├── core/
│   │   ├── config.py
│   │   └── logging.py
│   └── tests/
│       ├── test_status.py
│       └── test_tasks.py
├── requirements.txt
└── README.md
```

## Directory purpose

- `backend/`: Contains the Python backend source tree and tests.
- `backend/app/`: Contains the FastAPI application factory and runtime entry point used by Uvicorn.
- `backend/api/`: Contains API routers and endpoint definitions.
- `backend/models/`: Contains SQLAlchemy ORM models that map Python classes to database tables.
- `backend/schemas/`: Contains Pydantic schemas for request validation and response serialization.
- `backend/services/`: Contains business logic separated from HTTP route handlers.
- `backend/database/`: Contains database metadata, engine, and session configuration.
- `backend/core/`: Contains shared core configuration such as environment settings and logging.
- `backend/tests/`: Contains automated tests for the backend.
- `requirements.txt`: Defines Python package dependencies for local development and, later, Docker image builds.
- `README.md`: Documents the project, milestone status, and learning notes.

## API endpoints

| Method | Path | Purpose |
| --- | --- | --- |
| `GET` | `/` | Basic service status. |
| `GET` | `/health` | Lightweight health check. |
| `POST` | `/tasks` | Create a task. |
| `GET` | `/tasks` | List tasks. |
| `GET` | `/tasks/{id}` | Get one task. |
| `PUT` | `/tasks/{id}` | Replace one task. |
| `DELETE` | `/tasks/{id}` | Delete one task. |

## Task model

A task contains these fields:

- `id`: Integer primary key assigned by the database.
- `title`: Required task title.
- `description`: Optional longer task description.
- `completed`: Boolean completion flag.
- `created_at`: UTC timestamp set when the task is created.
- `updated_at`: UTC timestamp updated when the task changes.

## Running locally

From the `task-manager/backend` directory, run:

```bash
uvicorn app.main:app --reload
```

The application is then available at `http://127.0.0.1:8000`.

## SQLAlchemy

SQLAlchemy is the database toolkit used by this milestone. The `Task` ORM class describes the `tasks` table as Python code, while SQLAlchemy converts service operations into SQL statements for SQLite.

## Sessions

A database session is created per request by the `get_db()` dependency. Route handlers receive the session through FastAPI dependency injection, use it for one unit of work, and the dependency closes it after the request finishes.

## ORM

The ORM lets the application work with `Task` Python objects instead of manually writing SQL for every operation. This keeps CRUD logic readable while still preserving a clear database model.

## Pydantic

Pydantic schemas define the public API contract. Request schemas validate incoming JSON, and response schemas serialize ORM objects into safe JSON responses.

## Docker learning path

Docker will later copy this code into an image, install `requirements.txt`, run Uvicorn, and persist the SQLite file through a mounted volume during local container development.

## Kubernetes learning path

Kubernetes will later run this API in Pods. SQLite is useful for learning CRUD basics, but it stores data in a local file, which is not suitable for multi-replica production Pods. A later milestone will replace SQLite with PostgreSQL and persistent Kubernetes storage.
