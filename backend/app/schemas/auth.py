from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from uuid import UUID


class UserCreate(BaseModel):
    email: str
    password: str
    name: Optional[str] = None


class UserResponse(BaseModel):
    id: UUID
    email: str
    name: Optional[str]
    created_at: datetime
    token: Optional[str] = None


class LoginRequest(BaseModel):
    email: str
    password: str