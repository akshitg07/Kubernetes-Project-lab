"""FastAPI application entry point."""

import logging
<<<<<<< HEAD
from pathlib import Path
=======
>>>>>>> codex/create-project-skeleton-structure
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
<<<<<<< HEAD
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
=======
>>>>>>> codex/create-project-skeleton-structure

from api.routes import router as status_router
from api.tasks import router as tasks_router
from core.config import get_settings
from core.logging import configure_logging
from database.base import Base
from database.session import engine
from models.task import Task

logger = logging.getLogger(__name__)
_registered_models = (Task,)
<<<<<<< HEAD
STATIC_DIR = Path(__file__).resolve().parents[1] / "static"
=======
>>>>>>> codex/create-project-skeleton-structure


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Manage application startup and shutdown events."""

    settings = get_settings()
    configure_logging(settings.log_level)
    Base.metadata.create_all(bind=engine)
    logger.debug("Registered ORM models: %s", [model.__name__ for model in _registered_models])
    logger.info("Starting %s in %s mode", settings.app_name, settings.environment)
    yield
    logger.info("Stopping %s", settings.app_name)


def create_app() -> FastAPI:
    """Create and configure the FastAPI application instance."""

    settings = get_settings()
    application = FastAPI(title=settings.app_name, lifespan=lifespan)
<<<<<<< HEAD
    application.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
    application.include_router(status_router)
    application.include_router(tasks_router)

    @application.get("/ui", include_in_schema=False)
    def read_ui() -> FileResponse:
        """Serve the browser UI for the Task Manager."""

        return FileResponse(STATIC_DIR / "index.html")
=======
    application.include_router(status_router)
    application.include_router(tasks_router)
>>>>>>> codex/create-project-skeleton-structure
    return application


app = create_app()
