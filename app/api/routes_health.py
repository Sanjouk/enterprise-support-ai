from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get(
    "/health", summary="Health Check", description="Check if the API is running."
)
def health_check() -> dict[str, str]:
    return {"status": "ok"}
