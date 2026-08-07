"""Application configuration loaded from environment variables."""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime settings for the Task Manager API."""

    app_name: str = "Task Manager API"
    environment: str = "development"
    log_level: str = "INFO"

    model_config = SettingsConfigDict(env_prefix="TASK_MANAGER_", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    """Return cached application settings for dependency injection."""

    return Settings()
