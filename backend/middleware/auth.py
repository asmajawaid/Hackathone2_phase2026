
from fastapi import HTTPException, Header, Depends
from jose import jwt, JWTError
import os
from dotenv import load_dotenv

load_dotenv()

BETTER_AUTH_SECRET = os.getenv("BETTER_AUTH_SECRET")

async def verify_jwt(authorization: str = Header(...)) -> str:
    """
    Verify JWT token and extract user_id
    Usage: user_id = Depends(verify_jwt)
    """
    try:
        # Remove "Bearer " prefix
        if authorization.startswith("Bearer "):
            token = authorization[7:]
        else:
            token = authorization

        # Decode JWT
        payload = jwt.decode(
            token,
            BETTER_AUTH_SECRET,
            algorithms=["HS256"]
        )

        # Extract user_id
        user_id = payload.get("user_id") or payload.get("sub")

        if not user_id:
            raise HTTPException(
                status_code=401,
                detail="Invalid token: user_id not found"
            )

        return user_id

    except JWTError as e:
        raise HTTPException(
            status_code=401,
            detail=f"Invalid token: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=401,
            detail="Authentication required"
        )

async def get_current_user_id(user_id: str = Depends(verify_jwt)) -> str:
    """Dependency to get current authenticated user ID"""
    return user_id
