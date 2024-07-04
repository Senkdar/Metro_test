from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.settings import get_db
from app.logic.news import get_news_by_days
from app.utils.parser import parse_news
from app.schemas import NewsCreateSchema, NewsGetSchema


router = APIRouter()


@router.get(
    "/get_news",
    summary="Получение новостей",
    status_code=status.HTTP_200_OK,
    response_model=list[NewsGetSchema],
    responses={
        status.HTTP_200_OK: {"description": "Получение новостей за последние n дней"},
    },
)
async def read_news(
    days: int, db: AsyncSession = Depends(get_db)
) -> list[NewsGetSchema]:
    news = await get_news_by_days(db, days=days)
    return news


# Добавил, чтобы можно было не ждать запуска по расписанию
@router.post(
    "/create_news",
    response_model=list[NewsCreateSchema],
    status_code=status.HTTP_201_CREATED,
    summary="Парсинг новостей",
)
async def create_news() -> list[NewsCreateSchema]:
    news = await parse_news()
    return news
