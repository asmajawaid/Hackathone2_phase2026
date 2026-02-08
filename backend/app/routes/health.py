from fastapi import APIRouter
from app.schemas.common import SuccessResponse


router = APIRouter()


@router.get("/health", response_model=SuccessResponse)
def health_check():
    """Health check endpoint to verify the API is running"""
    return SuccessResponse(
        data={"status": "healthy", "message": "API is running"},
        message="Health check successful"
    )