from typing import List, Optional
from sqlmodel import Session, select
from app.models import Task, TaskStatus
from app.repositories.base import BaseRepository


class TaskRepository(BaseRepository[Task]):
    def __init__(self, session: Session):
        super().__init__(session, Task)

    def get_tasks_by_user_id(
        self,
        user_id: str,
        skip: int = 0,
        limit: int = 100,
        status: Optional[TaskStatus] = None
    ) -> List[Task]:
        statement = select(Task).where(Task.user_id == user_id)

        if status:
            statement = statement.where(Task.status == status)

        statement = statement.offset(skip).limit(limit).order_by(Task.created_at.desc())
        return self.session.exec(statement).all()

    def get_task_by_user_and_id(self, user_id: str, task_id: str) -> Optional[Task]:
        statement = select(Task).where(Task.user_id == user_id, Task.id == task_id)
        return self.session.exec(statement).first()

    def update_task(self, user_id: str, task_id: str, task: Task) -> Optional[Task]:
        existing_task = self.get_task_by_user_and_id(user_id, task_id)
        if existing_task:
            for key, value in task.__dict__.items():
                if hasattr(existing_task, key) and key != '_sa_instance_state':
                    setattr(existing_task, key, value)
            self.session.add(existing_task)
            self.session.commit()
            self.session.refresh(existing_task)
            return existing_task
        return None

    def delete_task_by_user_and_id(self, user_id: str, task_id: str) -> bool:
        task = self.get_task_by_user_and_id(user_id, task_id)
        if task:
            self.session.delete(task)
            self.session.commit()
            return True
        return False

    def toggle_completion(self, user_id: str, task_id: str) -> Optional[Task]:
        task = self.get_task_by_user_and_id(user_id, task_id)
        if task:
            task.completed = not task.completed
            self.session.add(task)
            self.session.commit()
            self.session.refresh(task)
            return task
        return None