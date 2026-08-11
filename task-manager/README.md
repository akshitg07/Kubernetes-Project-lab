# Task Manager API

This project is a Kubernetes learning lab that will grow incrementally into a production-quality Task Manager API.

## Current milestone: Milestone 4 — Containerized application

Milestone 4 containerizes the FastAPI Task Manager application with Docker and Docker Compose. The app still uses SQLite, and Compose persists the database with a named volume.

## Project structure

```text
task-manager/
├── Dockerfile
├── .dockerignore
├── docker-compose.yml
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
│   ├── static/
│   │   ├── app.js
│   │   ├── index.html
│   │   └── styles.css
│   └── tests/
│       ├── test_status.py
│       └── test_tasks.py
├── requirements.txt
└── README.md
```

## Directory purpose

- `Dockerfile`: Defines how to build the production-style container image for the FastAPI application.
- `.dockerignore`: Keeps local-only files out of the Docker build context so builds are smaller and more repeatable.
- `docker-compose.yml`: Runs the API locally as a container with port mapping, environment variables, a health check, and a persistent SQLite volume.
- `backend/`: Contains the Python backend source tree and tests.
- `backend/app/`: Contains the FastAPI application factory and runtime entry point used by Uvicorn.
- `backend/api/`: Contains API routers and endpoint definitions.
- `backend/models/`: Contains SQLAlchemy ORM models that map Python classes to database tables.
- `backend/schemas/`: Contains Pydantic schemas for request validation and response serialization.
- `backend/services/`: Contains business logic separated from HTTP route handlers.
- `backend/database/`: Contains database metadata, engine, and session configuration.
- `backend/core/`: Contains shared core configuration such as environment settings and logging.
- `backend/static/`: Contains the browser UI assets served by FastAPI at `/ui`.
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
| `GET` | `/ui` | Browser UI for managing tasks. |

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

The API is then available at `http://127.0.0.1:8000`, and the browser UI is available at `http://127.0.0.1:8000/ui`.

## Browser UI

The browser UI is intentionally static HTML, CSS, and JavaScript served by FastAPI. It calls the same `/tasks` API endpoints that command-line clients and future frontend deployments would use. Keeping the UI static avoids adding a frontend build toolchain while still making the application easy to demo.

## SQLAlchemy

SQLAlchemy is the database toolkit used by this milestone. The `Task` ORM class describes the `tasks` table as Python code, while SQLAlchemy converts service operations into SQL statements for SQLite.

## Sessions

A database session is created per request by the `get_db()` dependency. Route handlers receive the session through FastAPI dependency injection, use it for one unit of work, and the dependency closes it after the request finishes.

## ORM

The ORM lets the application work with `Task` Python objects instead of manually writing SQL for every operation. This keeps CRUD logic readable while still preserving a clear database model.

## Pydantic

Pydantic schemas define the public API contract. Request schemas validate incoming JSON, and response schemas serialize ORM objects into safe JSON responses.

## Docker

Docker packages the application code, Python runtime, dependencies, and Uvicorn command into a reusable image. The container listens on port `8000`, serves the API and `/ui`, and stores SQLite data under `/data` so a volume can persist it.

### Build the image

```bash
docker build -t task-manager-api:local .
```

### Run one container

```bash
docker run --rm -p 8000:8000 -v task-manager-data:/data task-manager-api:local
```

### Run with Docker Compose

```bash
docker compose up --build
```

## Image

A Docker image is a versioned filesystem and metadata bundle. This project image starts from `python:3.12-slim`, installs the pinned Python dependencies, copies the backend source, and defines the Uvicorn command.

## Layer caching

The Dockerfile copies `requirements.txt` before the backend source. Docker can reuse the dependency installation layer when application code changes but dependencies do not, which makes repeated builds faster.

## Multi-stage builds

A multi-stage build uses multiple `FROM` stages to separate build tools from the final runtime image. We are not implementing that yet because the current app has no compiled frontend or native build step, but it will become useful when images need to be smaller or build dependencies need to be excluded from runtime.

## Container networking

Inside the container, Uvicorn binds to `0.0.0.0:8000` so Docker can forward traffic into it. Docker Compose creates a private network where services can reach each other by service name, which will matter when PostgreSQL is introduced later.

## Port mapping

The mapping `8000:8000` publishes container port `8000` on host port `8000`, so you can open `http://127.0.0.1:8000/ui` from your machine.

## Volumes

The Compose file mounts a named volume at `/data`. The SQLite database path points there, so task data survives container restarts and rebuilds.

## Kubernetes learning path

Kubernetes will later run the Docker image created in this milestone inside Pods. The same container port, environment variables, health endpoint, and volume concepts introduced here map directly to Kubernetes Deployments, Services, ConfigMaps, Secrets, probes, and persistent storage. SQLite is still temporary and will later be replaced with PostgreSQL.
