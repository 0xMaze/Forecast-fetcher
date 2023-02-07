from fastapi import APIRouter

from api.routes import weather

router = APIRouter()

router.include_router(weather.router, tags=["weather"], prefix="")
