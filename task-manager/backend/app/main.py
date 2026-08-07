"""FastAPI application entry point."""

import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.routes import router as status_router
from core.config import get_settings
from core.logging import configure_logging

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Manage application startup and shutdown events."""

    settings = get_settings()
    configure_logging(settings.log_level)
    logger.info("Starting %s in %s mode", settings.app_name, settings.environment)
    yield
    logger.info("Stopping %s", settings.app_name)


def create_app() -> FastAPI:
    """Create and configure the FastAPI application instance."""

    settings = get_settings()
    application = FastAPI(title=settings.app_name, lifespan=lifespan)
    application.include_router(status_router)
    return application


app = create_app()
