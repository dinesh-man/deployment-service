from fastapi import FastAPI

from contextlib import asynccontextmanager
from app.api.deployment import router as deployment_router

from app.db.database import Base
from app.db.session import engine

from app.db.seed import seed_data

from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

Base.metadata.create_all(bind=engine)

seed_data()

app = FastAPI(
    title="Deployment Service API",
    version="1.0.0"
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    seed_data()
    yield
    
app.include_router(deployment_router)

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

"""HTTP exception handler"""
@app.exception_handler(HTTPException)
async def http_exception_handler(
    request: Request,
    exc: HTTPException
):

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "message": exc.detail,
                "status_code": exc.status_code
            }
        }
    )

"""Generic exception handler"""
@app.exception_handler(Exception)
async def generic_exception_handler(
    request: Request,
    exc: Exception
):

    return JSONResponse(
        status_code=500,
        content={
            "error": {
                "message": "Internal server error",
                "status_code": 500
            }
        }
    )