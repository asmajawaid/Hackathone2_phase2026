from fastapi import HTTPException, status
from fastapi.security.http import HTTPAuthorizationCredentials
from app.utils.jwt import verify_token
from app.models import User
from app.repositories.user_repository import UserRepository
from app.database import engine
from sqlmodel import Session


async def authenticate_user(token: str) -> User:
    """
    Authenticate a user based on the provided JWT token
    """
    # Verify the token
    payload = verify_token(token)

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Extract user_id from the payload
    user_id = payload.get("sub")

    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Get user from database
    with Session(engine) as session:
        user_repo = UserRepository(session)
        user = user_repo.get_by_id(user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def verify_user_owns_resource(authenticated_user_id: str, resource_user_id: str) -> bool:
    """
    Verify that the authenticated user owns the resource
    """
    return authenticated_user_id == resource_user_id