"""Pydantic schemas for task requests and responses."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class TaskBase(BaseModel):
    """Shared task fields."""

    title: str = Field(min_length=1, max_length=200)
    description: str | None = None
    completed: bool = False


class TaskCreate(TaskBase):
    """Request body for creating a task."""


class TaskUpdate(BaseModel):
    """Request body for replacing an existing task."""

    title: str = Field(min_length=1, max_length=200)
    description: str | None = None
    completed: bool


class TaskRead(TaskBase):
    """Response body for task resources."""

    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
