from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlmodel import Session
from app.database import get_session
from app.services.auth import get_current_user
from app.models import User, Task
from app.schemas.task import TaskResponse, TaskCreate, TaskUpdate, TaskToggleCompletion
from app.schemas.common import SuccessResponse
from app.repositories.task_repository import TaskRepository
from app.errors import ResourceNotFoundError, AuthorizationError
from uuid import UUID

router = APIRouter()


@router.get("/{user_id}/tasks", response_model=SuccessResponse)
def get_tasks(
    user_id: str,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, le=100, ge=1),
    status: Optional[str] = Query(None),
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Get all tasks for a user with optional filtering and pagination"""
    if str(current_user.id) != user_id:
        raise AuthorizationError("Not authorized to access this user's tasks")

    task_repo = TaskRepository(session)
    tasks = task_repo.get_tasks_by_user_id(
        user_id=user_id,
        skip=skip,
        limit=limit,
        status=status
    )

    # Convert to response format manually since from_orm doesn't work with SQLModel
    task_responses = []
    for task in tasks:
        task_responses.append(TaskResponse(
            id=task.id,
            user_id=task.user_id,
            title=task.title,
            description=task.description,
            status=task.status,
            priority=task.priority,
            completed=task.completed,
            created_at=task.created_at,
            updated_at=task.updated_at
        ))

    return SuccessResponse(
        data={
            "tasks": task_responses,
            "pagination": {
                "total": len(tasks),  # This should be actual total count
                "limit": limit,
                "offset": skip,
                "has_more": len(tasks) == limit
            }
        },
        message="Tasks retrieved successfully"
    )


@router.post("/{user_id}/tasks", response_model=SuccessResponse)
def create_task(
    user_id: str,
    task_create: TaskCreate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Create a new task for the authenticated user"""
    if str(current_user.id) != user_id:
        raise AuthorizationError("Not authorized to create tasks for this user")

    # Create task instance
    task = Task(
        user_id=user_id,
        title=task_create.title,
        description=task_create.description,
        status=task_create.status,
        priority=task_create.priority
    )

    task_repo = TaskRepository(session)
    created_task = task_repo.create(task)

    # Convert to response format manually
    task_response = TaskResponse(
        id=created_task.id,
        user_id=created_task.user_id,
        title=created_task.title,
        description=created_task.description,
        status=created_task.status,
        priority=created_task.priority,
        completed=created_task.completed,
        created_at=created_task.created_at,
        updated_at=created_task.updated_at
    )

    return SuccessResponse(
        data={"task": task_response},
        message="Task created successfully"
    )


@router.get("/{user_id}/tasks/{id}", response_model=SuccessResponse)
def get_task(
    user_id: str,
    id: UUID,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Get a specific task by ID for the authenticated user"""
    if str(current_user.id) != user_id:
        raise AuthorizationError("Not authorized to access this user's tasks")

    task_repo = TaskRepository(session)
    task = task_repo.get_task_by_user_and_id(user_id, str(id))

    if not task:
        raise ResourceNotFoundError("Task not found")

    # Convert to response format manually
    task_response = TaskResponse(
        id=task.id,
        user_id=task.user_id,
        title=task.title,
        description=task.description,
        status=task.status,
        priority=task.priority,
        completed=task.completed,
        created_at=task.created_at,
        updated_at=task.updated_at
    )

    return SuccessResponse(
        data={"task": task_response},
        message="Task retrieved successfully"
    )


@router.put("/{user_id}/tasks/{id}", response_model=SuccessResponse)
def update_task(
    user_id: str,
    id: UUID,
    task_update: TaskUpdate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Update a specific task for the authenticated user"""
    if str(current_user.id) != user_id:
        raise AuthorizationError("Not authorized to update this user's tasks")

    task_repo = TaskRepository(session)
    existing_task = task_repo.get_task_by_user_and_id(user_id, str(id))

    if not existing_task:
        raise ResourceNotFoundError("Task not found")

    # Update task fields
    for field, value in task_update.__dict__.items():
        if value is not None:
            setattr(existing_task, field, value)

    updated_task = task_repo.update(str(id), existing_task)

    # Convert to response format manually
    task_response = TaskResponse(
        id=updated_task.id,
        user_id=updated_task.user_id,
        title=updated_task.title,
        description=updated_task.description,
        status=updated_task.status,
        priority=updated_task.priority,
        completed=updated_task.completed,
        created_at=updated_task.created_at,
        updated_at=updated_task.updated_at
    )

    return SuccessResponse(
        data={"task": task_response},
        message="Task updated successfully"
    )


@router.delete("/{user_id}/tasks/{id}", response_model=SuccessResponse)
def delete_task(
    user_id: str,
    id: UUID,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Delete a specific task for the authenticated user"""
    if str(current_user.id) != user_id:
        raise AuthorizationError("Not authorized to delete this user's tasks")

    task_repo = TaskRepository(session)
    success = task_repo.delete_task_by_user_and_id(user_id, str(id))

    if not success:
        raise ResourceNotFoundError("Task not found")

    return SuccessResponse(
        data={},
        message="Task deleted successfully"
    )


@router.patch("/{user_id}/tasks/{id}/complete", response_model=SuccessResponse)
def toggle_task_completion(
    user_id: str,
    id: UUID,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Toggle the completion status of a specific task for the authenticated user"""
    if str(current_user.id) != user_id:
        raise AuthorizationError("Not authorized to update this user's tasks")

    task_repo = TaskRepository(session)
    task = task_repo.toggle_completion(user_id, str(id))

    if not task:
        raise ResourceNotFoundError("Task not found")

    # Convert to response format manually
    task_response = TaskResponse(
        id=task.id,
        user_id=task.user_id,
        title=task.title,
        description=task.description,
        status=task.status,
        priority=task.priority,
        completed=task.completed,
        created_at=task.created_at,
        updated_at=task.updated_at
    )

    return SuccessResponse(
        data={"task": task_response},
        message="Task completion toggled successfully"
    )