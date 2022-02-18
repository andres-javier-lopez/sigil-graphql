from os import path
from functools import wraps

from alembic import command
from alembic.config import Config

from sigil.store.adapters.psql import engine, async_session
from sigil.store.adapters.psql.models.base import Base
from sigil.store.interfaces import CampaignStore

dirname = path.dirname(__file__)
alembic_ini = path.join(dirname, 'alembic.ini')


def run_stamp(connection, cfg):
    cfg.attributes['connection'] = connection
    command.stamp(cfg, 'head')


async def init_storage():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

        alembic_cfg = Config(alembic_ini)
        await conn.run_sync(run_stamp, alembic_cfg)


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
