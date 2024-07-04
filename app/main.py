from fastapi import FastAPI
from apscheduler.schedulers.asyncio import AsyncIOScheduler

import app.config as config
from app.db.settings import Base, engine
from app.api.routes import router
from app.utils.parser import parse_news


app = FastAPI()

app.include_router(router)

scheduler = AsyncIOScheduler()


@app.on_event("startup")
async def on_startup():
    """Логика при запуске приложения."""

    # при запуске приложения таблица будет создана, но можно было бы и алембик добавить

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    scheduler.add_job(parse_news, "interval", minutes=config.MINUTES_TO_START_PARSING)
    scheduler.start()


@app.on_event("shutdown")
async def on_shutdown():
    """Логика при остановке приложения."""

    scheduler.shutdown()
