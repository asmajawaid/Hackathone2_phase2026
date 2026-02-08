from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import create_db_and_tables  # ⬅️ Add this
from app.routes import router as api_router
from app.config import settings

app = FastAPI(
    title="Todo Backend API",
    description="Backend API for the Evolution of Todo - Phase 2 Full-Stack Web Application",
    version="0.1.0",
    openapi_url="/api/v1/openapi.json"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins_list,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS", "HEAD"],
    allow_headers=["Authorization", "Content-Type", "X-Requested-With", "Accept"]
)

# Include API routes
app.include_router(api_router, prefix="/api/v1", tags=["tasks"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo Backend API"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "message": "API is running"}

# ⬅️ Add this event
@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    print("Database tables created")