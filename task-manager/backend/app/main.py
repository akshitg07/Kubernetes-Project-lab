"""FastAPI application entry point."""

import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.routes import router as status_router
from api.tasks import router as tasks_router
from core.config import get_settings
from core.logging import configure_logging
from database.base import Base
from database.session import engine
from models.task import Task

logger = logging.getLogger(__name__)
_registered_models = (Task,)


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
    application.include_router(status_router)
    application.include_router(tasks_router)
    return application


app = create_app()
