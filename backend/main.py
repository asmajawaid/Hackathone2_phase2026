
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Import database and models BEFORE creating app
from db import create_db_and_tables, engine
from models import User, Task  # CRITICAL: Import models before create_db_and_tables

# Create FastAPI app
app = FastAPI(
    title="Todo API",
    version="1.0.0",
    description="Phase 2 Todo Application API"
)

# Root Endpoint
@app.get("/")
async def root():
    return {
        "message": "Welcome to the Todo API",
        "docs": "/docs",
        "health": "/health"
    }

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://your-app.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Startup Event - Create Tables
@app.on_event("startup")
async def startup_event():
    """Create database tables on startup"""
    print("Starting application...")
    try:
        create_db_and_tables()
        print("Database tables created/verified successfully")

        # Test database connection
        from sqlmodel import Session, select
        with Session(engine) as session:
            # Check if tables exist by counting users
            result = session.exec(select(User)).first()
            print(f"Database connection verified")
    except Exception as e:
        print(f"Database error on startup: {e}")
        raise

# Health check endpoint
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "database": "connected",
        "version": "1.0.0"
    }

# Import and include routers
from routes import tasks
app.include_router(tasks.router, prefix="/api", tags=["tasks"])

# Better Auth routes (if using Better Auth)
try:
    from lib.auth import auth_router
    app.include_router(auth_router, prefix="/api/auth", tags=["auth"])
except ImportError:
    print("Better Auth routes not found - using manual auth")

# Manual Auth routes (if Better Auth is not set up or fails)
from routes import auth
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
