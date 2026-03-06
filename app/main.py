from fastapi import FastAPI

from app.api.routes_health import router as health_router


app = FastAPI(
    title="AI Support Copilot",
    description="Business-oriented support copilot with RAG and tool calling.",
    version="0.1.0",
)


@app.get("/", tags=["root"])
def root() -> dict[str, str]:
    return {"message": "AI Support Copilot API is running"}


app.include_router(health_router)
