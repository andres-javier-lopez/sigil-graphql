from contextlib import asynccontextmanager

from sigil.storage.adapters.psql import async_session
from sigil.storage.adapters.psql.storages import (
    CampaignStorage,
    HubStorage,
    PartyStorage,
    PlayerCharacterStorage,
)


class StorageManager:
    def __init__(self, session):
        self.session = session
        self._campaign_storage = None
        self._hub_storage = None
        self._party_storage = None
        self._player_character_storage = None

    @property
    def campaign_storage(self):
        if self._campaign_storage is None:
            self._campaign_storage = CampaignStorage(self.session)

        return self._campaign_storage

    @property
    def hub_storage(self):
        if self._hub_storage is None:
            self._hub_storage = HubStorage(self.session)

        return self._hub_storage

    @property
    def party_storage(self):
        if self._party_storage is None:
            self._party_storage = PartyStorage(self.session)

        return self._party_storage

    @property
    def player_character_storage(self):
        if self._player_character_storage is None:
            self._player_character_storage = PlayerCharacterStorage(self.session)

        return self._player_character_storage

    @classmethod
    @asynccontextmanager
    async def start(cls):
        async with async_session() as session:
            yield cls(session)
