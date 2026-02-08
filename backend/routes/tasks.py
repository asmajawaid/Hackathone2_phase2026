from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select, SQLModel
from typing import List
from datetime import datetime

from db import get_session
from models import Task
from middleware.auth import get_current_user_id

router = APIRouter()

class TaskCreate(SQLModel):
    title: str
    description: str | None = None
    completed: bool = False

@router.get("/", response_model=List[Task])
async def get_tasks(
    session: Session = Depends(get_session),
    user_id: str = Depends(get_current_user_id)
):
    tasks = session.exec(select(Task).where(Task.user_id == user_id)).all()
    return tasks

@router.post("/", response_model=Task)
async def create_task(
    task_create: TaskCreate,
    session: Session = Depends(get_session),
    user_id: str = Depends(get_current_user_id)
):
    task = Task.from_orm(task_create)
    task.user_id = user_id
    task.created_at = datetime.utcnow()
    task.updated_at = datetime.utcnow()
    session.add(task)
    session.commit()
    session.refresh(task)
    return task
