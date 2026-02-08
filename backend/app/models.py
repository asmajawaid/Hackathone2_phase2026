from datetime import datetime
from enum import Enum
from uuid import UUID, uuid4
from typing import Optional
from sqlmodel import Field, SQLModel
from sqlalchemy import Column, String, Index


class TaskStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


class TaskPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    email: str = Field(sa_column=Column(String, unique=True, nullable=False))
    name: Optional[str] = None
    password_hash: str = Field(sa_column=Column(String, nullable=False))  # Add password hash field
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class Task(SQLModel, table=True):
    __tablename__ = "tasks"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    user_id: UUID = Field(foreign_key="users.id", ondelete="CASCADE")
    title: str = Field(sa_column=Column(String(200), nullable=False))
    description: Optional[str] = None
    status: TaskStatus = Field(default=TaskStatus.PENDING)
    priority: TaskPriority = Field(default=TaskPriority.MEDIUM)
    completed: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Define indexes
    __table_args__ = (
        Index("idx_user_status", "user_id", "status"),
        Index("idx_user_created", "user_id", "created_at"),
    )