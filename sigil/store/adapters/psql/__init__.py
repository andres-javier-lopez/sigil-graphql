from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.future import select as future_select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import Select

from sigil import settings


def get_connection_string():
    return create_connection_string(
        settings.DB_USER,
        settings.DB_PASSWORD,
        settings.DB_HOST,
        settings.DB_PORT,
        settings.DB_NAME,
    )


def create_connection_string(user, password, host, port, db):
    return f'postgresql+asyncpg://{user}:{password}@{host}:{port}/{db}'


engine = create_async_engine(get_connection_string())

Session: AsyncSession = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


def select(*entities) -> Select:
    """Wrapper for future select to improve typing"""
    return future_select(*entities)
