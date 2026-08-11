"""HTTP route definitions for service status endpoints."""

from typing import Annotated

from fastapi import APIRouter, Depends

from core.config import Settings, get_settings

router = APIRouter(tags=["status"])


@router.get("/", summary="Read application status")
def read_root(settings: Annotated[Settings, Depends(get_settings)]) -> dict[str, str]:
    """Return a basic health response for humans and simple platform checks."""

    return {"status": "healthy"}


@router.get("/health", summary="Read health check status")
def read_health() -> dict[str, str]:
    """Return a lightweight health response for orchestrators and load balancers."""

    return {"status": "ok"}
