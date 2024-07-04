from datetime import datetime, timedelta, timezone

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.db.tables import News
from app.schemas import NewsCreateSchema, NewsGetSchema


async def get_news_by_days(db: AsyncSession, days: int):
    """Получение новостей за последние n дней."""

    # безопаснее явно указать таймзону, поэтому - timezone.utc
    last_date = datetime.now(timezone.utc) - timedelta(days=days)
    result = await db.execute(select(News).filter(News.publication_date >= last_date))
    news_list = result.scalars().all()

    return [NewsGetSchema.from_orm(news) for news in news_list]


async def create_news(db: AsyncSession, news: list[NewsCreateSchema]):
    """Создание объектов новостей в базе."""

    for item in news:
        db_news = News(**item.dict())
        db.add(db_news)

    await db.commit()

    return news
