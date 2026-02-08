from typing import Any, Optional
from pydantic import BaseModel


class SuccessResponse(BaseModel):
    success: bool = True
    data: Optional[Any] = None
    message: str = "Operation successful"


class ErrorResponse(BaseModel):
    success: bool = False
    error: str
    code: str
    details: Optional[dict] = None