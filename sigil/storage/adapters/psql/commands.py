from os import path

from alembic import command
from alembic.config import Config

from sigil.storage.adapters.psql import engine
from sigil.storage.adapters.psql.models.base import Base

dirname = path.dirname(__file__)
alembic_ini = path.join(dirname, "alembic.ini")


def _run_stamp(connection, cfg):
    cfg.attributes["connection"] = connection
    command.stamp(cfg, "head")


async def init_storage():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

        alembic_cfg = Config(alembic_ini)
        await conn.run_sync(_run_stamp, alembic_cfg)


def _run_upgrade(connection, cfg):
    cfg.attributes["connection"] = connection
    command.upgrade(cfg, "head")


async def upgrade_storage():
    async with engine.begin() as conn:
        alembic_cfg = Config(alembic_ini)
        await conn.run_sync(_run_upgrade, alembic_cfg)
