from functools import wraps

from sigil.store.adapters.psql import engine, async_session
from sigil.store.adapters.psql.models.base import Base
from sigil.store.interfaces import CampaignStore


async def init_storage():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


def seed_stores(func):
    @wraps(func)
    async def _seed_with_stores(*args, **kwargs):
        async with async_session() as session:
            async with session.begin():
                stores = {
                    CampaignStore.__name__: CampaignStore(session),
                }
                await func(*args, **kwargs, stores=stores)

                await session.commit()
        await engine.dispose()

    return _seed_with_stores
