from abc import abstractmethod
from typing import List, Optional

from pydantic import UUID4

from sigil.domain.entities import Campaign, PlayerCharacter
from sigil.domain.mocks import mock_campaigns, mock_player_characters
from sigil.storage.base import BaseStorage


class BaseCampaignStorage(BaseStorage):
    @abstractmethod
    async def list(self, filter: dict = None) -> List[Campaign]:
        raise NotImplementedError

    @abstractmethod
    async def get(self, uuid: UUID4) -> Optional[Campaign]:
        raise NotImplementedError

    @abstractmethod
    async def save(self, entity: Campaign):
        raise NotImplementedError

    @abstractmethod
    async def save_all(self, entities: List[Campaign]):
        raise NotImplementedError


async def seed_campaigns(storage: BaseCampaignStorage, number=5) -> List[Campaign]:
    campaigns = mock_campaigns(number=number)
    await storage.save_all(campaigns)
    return campaigns


class BasePlayerCharacterStorage(BaseStorage):
    @abstractmethod
    async def list(self, filter: dict = None) -> List[PlayerCharacter]:
        raise NotImplementedError

    @abstractmethod
    async def get(self, uuid: UUID4) -> Optional[PlayerCharacter]:
        raise NotImplementedError

    @abstractmethod
    async def save(self, entity: PlayerCharacter):
        raise NotImplementedError

    @abstractmethod
    async def save_all(self, entities: List[PlayerCharacter]):
        raise NotImplementedError


async def seed_player_characters(
    storage: BasePlayerCharacterStorage, campaign: Campaign, number=4
) -> List[PlayerCharacter]:
    player_characters = mock_player_characters(campaign, number=number)
    await storage.save_all(player_characters)
    return player_characters
