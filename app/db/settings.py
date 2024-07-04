from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app import config

DATABASE_URL = config.DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession
)

Base = declarative_base()


async def get_db() -> AsyncSession:
    async with SessionLocal() as session:
        yield session
