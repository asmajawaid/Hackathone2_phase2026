from fastapi.middleware.cors import CORSMiddleware
from app.config import settings


def setup_cors_middleware(app):
    """Setup CORS middleware for the application"""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_origins_list,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
        allow_headers=["*"],
        # Allow the authorization header specifically
        allow_headers=["Authorization", "Content-Type", "X-Requested-With"],
    )