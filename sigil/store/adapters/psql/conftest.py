import pytest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from sigil import settings
from sigil.store.adapters.psql import create_connection_string
from sigil.store.adapters.psql.models import Base


@pytest.fixture
async def psql_session():
    engine = create_async_engine(
        create_connection_string(
            settings.DB_TEST_USER,
            settings.DB_TEST_PASSWORD,
            settings.DB_TEST_HOST,
            settings.DB_TEST_PORT,
            settings.DB_TEST_NAME,
        )
    )

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    Session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    session: AsyncSession = Session()
    yield session
    await session.rollback()
    await session.close()
