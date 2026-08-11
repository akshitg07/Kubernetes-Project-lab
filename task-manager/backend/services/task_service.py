"""Business logic for task resources."""

from sqlalchemy import select
from sqlalchemy.orm import Session

from models.task import Task
from schemas.task import TaskCreate, TaskUpdate


class TaskNotFoundError(Exception):
    """Raised when a task cannot be found."""


def create_task(db: Session, task_in: TaskCreate) -> Task:
    """Create and persist a task."""

    task = Task(**task_in.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def list_tasks(db: Session) -> list[Task]:
    """Return all tasks ordered by creation time."""

    return list(db.scalars(select(Task).order_by(Task.created_at.desc(), Task.id.desc())).all())


def get_task(db: Session, task_id: int) -> Task:
    """Return a task by ID or raise when it does not exist."""

    task = db.get(Task, task_id)
    if task is None:
        raise TaskNotFoundError(f"Task {task_id} was not found")
    return task


def update_task(db: Session, task_id: int, task_in: TaskUpdate) -> Task:
    """Replace a task with new field values."""

    task = get_task(db, task_id)
    for field, value in task_in.model_dump().items():
        setattr(task, field, value)
    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task_id: int) -> None:
    """Delete a task by ID."""

    task = get_task(db, task_id)
    db.delete(task)
    db.commit()
