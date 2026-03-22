from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.api.routes_health import router as health_router
from app.api.routes_tickets import router as tickets_router

PROJECT_ROOT = Path(__file__).resolve().parents[1]
FRONTEND_DIR = PROJECT_ROOT / "frontend"

app = FastAPI(
    title="Enterprise Support AI",
    description="Business-oriented support copilot with RAG and tool calling.",
    version="0.1.0",
)


@app.get("/", tags=["root"])
def root() -> dict[str, str]:
    return {
        "message": "Enterprise Support AI API is running",
        "ui": "/ui",
        "docs": "/docs",
    }


if FRONTEND_DIR.exists():
    app.mount("/ui/static", StaticFiles(directory=FRONTEND_DIR), name="ui-static")


def _frontend_file(path: str) -> Path:
    file_path = FRONTEND_DIR / path
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Frontend is not configured.")
    return file_path


@app.get("/ui", include_in_schema=False)
@app.get("/ui/", include_in_schema=False)
def frontend_ui() -> FileResponse:
    return FileResponse(_frontend_file("index.html"))


app.include_router(health_router)
app.include_router(tickets_router)
