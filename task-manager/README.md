# Task Manager API

This project is a Kubernetes learning lab that will grow incrementally into a production-quality Task Manager API.

## Current milestone: Milestone 3 — Task CRUD with SQLite

<<<<<<< HEAD
Milestone 3 adds a real Task resource with create, read, update, delete, and list operations backed by SQLite through SQLAlchemy. This version also includes a clean browser UI served at `/ui` so the API can be exercised without external tools.
=======
Milestone 3 adds a real Task resource with create, read, update, delete, and list operations backed by SQLite through SQLAlchemy.
>>>>>>> codex/create-project-skeleton-structure

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
<<<<<<< HEAD
│   ├── static/
│   │   ├── app.js
│   │   ├── index.html
│   │   └── styles.css
=======
>>>>>>> codex/create-project-skeleton-structure
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
<<<<<<< HEAD
- `backend/static/`: Contains the browser UI assets served by FastAPI at `/ui`.
=======
>>>>>>> codex/create-project-skeleton-structure
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
<<<<<<< HEAD
| `GET` | `/ui` | Browser UI for managing tasks. |
=======
>>>>>>> codex/create-project-skeleton-structure

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

<<<<<<< HEAD
The API is then available at `http://127.0.0.1:8000`, and the browser UI is available at `http://127.0.0.1:8000/ui`.

## Browser UI

The browser UI is intentionally static HTML, CSS, and JavaScript served by FastAPI. It calls the same `/tasks` API endpoints that command-line clients and future frontend deployments would use. Keeping the UI static avoids adding a frontend build toolchain while still making the application easy to demo.
=======
The application is then available at `http://127.0.0.1:8000`.
>>>>>>> codex/create-project-skeleton-structure

## SQLAlchemy

SQLAlchemy is the database toolkit used by this milestone. The `Task` ORM class describes the `tasks` table as Python code, while SQLAlchemy converts service operations into SQL statements for SQLite.

## Sessions

A database session is created per request by the `get_db()` dependency. Route handlers receive the session through FastAPI dependency injection, use it for one unit of work, and the dependency closes it after the request finishes.

## ORM

The ORM lets the application work with `Task` Python objects instead of manually writing SQL for every operation. This keeps CRUD logic readable while still preserving a clear database model.

## Pydantic

Pydantic schemas define the public API contract. Request schemas validate incoming JSON, and response schemas serialize ORM objects into safe JSON responses.

## Docker learning path

<<<<<<< HEAD
Docker will later copy this code into an image, install `requirements.txt`, run Uvicorn, serve the static UI assets, and persist the SQLite file through a mounted volume during local container development.

## Kubernetes learning path

Kubernetes will later run this API and UI in Pods. SQLite is useful for learning CRUD basics, but it stores data in a local file, which is not suitable for multi-replica production Pods. A later milestone will replace SQLite with PostgreSQL and persistent Kubernetes storage.
=======
Docker will later copy this code into an image, install `requirements.txt`, run Uvicorn, and persist the SQLite file through a mounted volume during local container development.

## Kubernetes learning path

Kubernetes will later run this API in Pods. SQLite is useful for learning CRUD basics, but it stores data in a local file, which is not suitable for multi-replica production Pods. A later milestone will replace SQLite with PostgreSQL and persistent Kubernetes storage.
>>>>>>> codex/create-project-skeleton-structure
