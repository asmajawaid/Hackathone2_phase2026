from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from uuid import UUID


class UserResponse(BaseModel):
    id: UUID
    email: str
    name: Optional[str]
    created_at: datetime
    updated_at: datetime
    token: Optional[str] = None