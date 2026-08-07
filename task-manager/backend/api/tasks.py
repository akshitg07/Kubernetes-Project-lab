"""HTTP routes for task CRUD operations."""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from database.session import get_db
from schemas.task import TaskCreate, TaskRead, TaskUpdate
from services import task_service
from services.task_service import TaskNotFoundError

router = APIRouter(prefix="/tasks", tags=["tasks"])

DbSession = Annotated[Session, Depends(get_db)]


def raise_not_found(task_id: int) -> None:
    """Raise a consistent HTTP 404 response for missing tasks."""

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task {task_id} not found")


@router.post("", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(task_in: TaskCreate, db: DbSession) -> TaskRead:
    """Create a new task."""

    return task_service.create_task(db, task_in)


@router.get("", response_model=list[TaskRead])
def list_tasks(db: DbSession) -> list[TaskRead]:
    """List all tasks."""

    return task_service.list_tasks(db)


@router.get("/{task_id}", response_model=TaskRead)
def get_task(task_id: int, db: DbSession) -> TaskRead:
    """Get a task by ID."""

    try:
        return task_service.get_task(db, task_id)
    except TaskNotFoundError:
        raise_not_found(task_id)


@router.put("/{task_id}", response_model=TaskRead)
def update_task(task_id: int, task_in: TaskUpdate, db: DbSession) -> TaskRead:
    """Replace a task by ID."""

    try:
        return task_service.update_task(db, task_id, task_in)
    except TaskNotFoundError:
        raise_not_found(task_id)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: DbSession) -> Response:
    """Delete a task by ID."""

    try:
        task_service.delete_task(db, task_id)
    except TaskNotFoundError:
        raise_not_found(task_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
