from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from uuid import UUID
from app.constants import TaskStatus, TaskPriority


class TaskResponse(BaseModel):
    id: UUID
    user_id: UUID
    title: str
    description: Optional[str]
    status: TaskStatus
    priority: TaskPriority
    completed: bool
    created_at: datetime
    updated_at: datetime


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[TaskStatus] = TaskStatus.PENDING
    priority: Optional[TaskPriority] = TaskPriority.MEDIUM


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None


class TaskToggleCompletion(BaseModel):
    # Empty model since PATCH endpoint doesn't require a body
    pass