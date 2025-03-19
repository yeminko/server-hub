from fastapi import APIRouter
import utils.schemas as schemas

# Initialize router for health-related endpoints
router = APIRouter(
    tags=["health"],
    responses={404: {"model": schemas.ErrorResponse}}
)


@router.get("/health",
            response_model=schemas.HealthResponse,
            summary="Health check",
            description="Check if the API is running properly")
def health_check():
    """Check if the API is running properly"""
    return {"status": "healthy", "message": "ServerHub API is running"}
