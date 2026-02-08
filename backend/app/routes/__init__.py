from fastapi import APIRouter
from app.routes.health import router as health_router
from app.routes.tasks import router as task_router
from app.routes.auth import router as auth_router


router = APIRouter()

# Include health check endpoints
router.include_router(health_router)

# Include task endpoints
router.include_router(task_router)

# Include auth endpoints (without prefix since auth router already has /auth prefix)
router.include_router(auth_router)