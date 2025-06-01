from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from src.config import settings


sync_engine = create_engine(
    url=settings.SYNC_DATABASE_URL,
    echo=True,
    # pool_size=settings.POOL_SIZE,
    # max_overflow=settings.MAX_OVERFLOW,
)

async_engine = create_async_engine(
    url=settings.ASYNC_DATABASE_URL,
    echo=True,
    # pool_size=settings.POOL_SIZE,
    # max_overflow=settings.MAX_OVERFLOW,
)

session_factory = sessionmaker(sync_engine)
async_session_factory = async_sessionmaker(async_engine, class_=AsyncSession)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_factory() as session:
        yield session