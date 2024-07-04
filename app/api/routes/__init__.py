from fastapi import APIRouter

from app.api.routes.news import router as news_router


router = APIRouter()

router.include_router(news_router, tags=["News"])
