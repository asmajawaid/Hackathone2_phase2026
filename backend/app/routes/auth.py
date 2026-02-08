from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
import os
import uuid
from typing import Optional

from app.database import get_session
from app.models import User
from app.schemas.auth import UserCreate, UserResponse, LoginRequest
from app.config import settings

router = APIRouter(prefix="/auth", tags=["auth"])

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(user_id: str) -> str:
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {
        "sub": user_id,
        "exp": expire.timestamp()
    }
    return jwt.encode(to_encode, settings.BETTER_AUTH_SECRET, algorithm=settings.JWT_ALGORITHM)

@router.post("/signup", response_model=UserResponse)
async def signup(
    user_data: UserCreate,
    session: Session = Depends(get_session)
):
    """User signup endpoint"""

    # Validate input
    if not user_data.email or not user_data.password:
        raise HTTPException(status_code=400, detail="Email and password required")

    if len(user_data.password) < 8:
        raise HTTPException(status_code=400, detail="Password must be at least 8 characters")

    # Check if user exists
    existing_user = session.exec(
        select(User).where(User.email == user_data.email)
    ).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create user with hashed password
    user = User(
        id=uuid.uuid4(),
        email=user_data.email,
        name=user_data.name or user_data.email.split('@')[0],
        password_hash=hash_password(user_data.password),  # Hash the password
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    # Create JWT token
    token = create_access_token(str(user.id))

    return UserResponse(
        id=user.id,
        email=user.email,
        name=user.name,
        created_at=user.created_at,
        token=token
    )

@router.post("/signin", response_model=UserResponse)
async def signin(
    login_data: LoginRequest,
    session: Session = Depends(get_session)
):
    """User signin endpoint"""

    # Find user
    user = session.exec(
        select(User).where(User.email == login_data.email)
    ).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    # Verify password
    if not verify_password(login_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    # Create JWT token
    token = create_access_token(str(user.id))

    return UserResponse(
        id=user.id,
        email=user.email,
        name=user.name,
        created_at=user.created_at,
        token=token
    )