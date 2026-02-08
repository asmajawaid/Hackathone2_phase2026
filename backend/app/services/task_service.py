from typing import List, Optional
from sqlmodel import Session
from app.models import Task
from app.schemas.task import TaskCreate, TaskUpdate
from app.repositories.task_repository import TaskRepository
from app.errors import ResourceNotFoundError


class TaskService:
    def __init__(self, session: Session):
        self.session = session
        self.task_repo = TaskRepository(session)

    def create_task(self, user_id: str, task_create: TaskCreate) -> Task:
        """Create a new task for the specified user"""
        task = Task(
            user_id=user_id,
            title=task_create.title,
            description=task_create.description,
            status=task_create.status,
            priority=task_create.priority
        )

        return self.task_repo.create(task)

    def get_tasks_by_user(
        self,
        user_id: str,
        skip: int = 0,
        limit: int = 100,
        status: Optional[str] = None
    ) -> List[Task]:
        """Get all tasks for a specific user with optional filtering"""
        return self.task_repo.get_tasks_by_user_id(
            user_id=user_id,
            skip=skip,
            limit=limit,
            status=status
        )

    def get_task_by_user_and_id(self, user_id: str, task_id: str) -> Optional[Task]:
        """Get a specific task for a user by ID"""
        return self.task_repo.get_task_by_user_and_id(user_id, task_id)

    def update_task(self, user_id: str, task_id: str, task_update: TaskUpdate) -> Optional[Task]:
        """Update a specific task for a user"""
        # First, verify the task belongs to the user
        existing_task = self.task_repo.get_task_by_user_and_id(user_id, task_id)
        if not existing_task:
            return None

        # Update task fields
        for field, value in task_update.__dict__.items():
            if value is not None:
                setattr(existing_task, field, value)

        return self.task_repo.update(task_id, existing_task)

    def delete_task(self, user_id: str, task_id: str) -> bool:
        """Delete a specific task for a user"""
        return self.task_repo.delete_task_by_user_and_id(user_id, task_id)

    def toggle_task_completion(self, user_id: str, task_id: str) -> Optional[Task]:
        """Toggle the completion status of a specific task for a user"""
        return self.task_repo.toggle_completion(user_id, task_id)