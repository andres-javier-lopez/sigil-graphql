from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.future import select as future_select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import Delete, Select
from sqlalchemy.sql import delete as sql_delete

from sigil import settings


def get_connection_string():
    if settings.DATABASE_URL:
        async_url = settings.DATABASE_URL.replace(
            "postgres://", "postgresql+asyncpg://"
        )
        return async_url

    return create_connection_string(
        settings.DB_USER,
        settings.DB_PASSWORD,
        settings.DB_HOST,
        settings.DB_PORT,
        settings.DB_NAME,
    )


def create_connection_string(user, password, host, port, db):
    return f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{db}"


engine = create_async_engine(get_connection_string())

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


def select(*entities) -> Select:
    """Wrapper for future select to improve typing"""
    return future_select(*entities)


def delete(*args, **kwargs) -> Delete:
    """Wrapper for delete to improve typing"""
    return sql_delete(*args, **kwargs)
