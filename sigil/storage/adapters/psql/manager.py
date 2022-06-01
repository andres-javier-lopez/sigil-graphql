import logging
from contextlib import asynccontextmanager

from sigil.storage.adapters.psql import async_session
from sigil.storage.adapters.psql.storages import (
    CampaignStorage,
    HubStorage,
    PartyStorage,
    PlayerCharacterStorage,
)
from sigil.storage.base import BaseManager

logger = logging.getLogger(__name__)


class StorageManager(BaseManager):
    def __init__(self, session):
        self.session = session

        self._storage_classes = {
            "campaign_storage": CampaignStorage,
            "hub_storage": HubStorage,
            "party_storage": PartyStorage,
            "player_character_storage": PlayerCharacterStorage,
        }

    def _init_storage(self, StorageClass):
        return StorageClass(self.session)

    @classmethod
    @asynccontextmanager
    async def start(cls):
        async with async_session() as session:
            async with session.begin():
                try:
                    yield cls(session)
                except Exception:
                    logger.exception("rolling back session")
                    await session.rollback()
                else:
                    await session.commit()
                finally:
                    await session.close()
