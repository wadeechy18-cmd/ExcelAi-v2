from fastapi import FastAPI

from app.api.routes.auth import router as auth_router
from app.api.routes.users import router as users_router

app = FastAPI(
    title="ExcelAI API",
    description="Backend API for ExcelAI",
    version="0.1.0",
)

# Authentication routes
app.include_router(auth_router)
app.include_router(users_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to ExcelAI API"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }