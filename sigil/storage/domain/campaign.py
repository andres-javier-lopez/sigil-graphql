from abc import abstractmethod
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import UUID4

from sigil.domain.entities import Campaign, Party, PlayerCharacter
from sigil.domain.mocks import mock_campaigns, mock_party, mock_player_characters
from sigil.storage.base import BaseStorage


class BaseCampaignStorage(BaseStorage):
    class FILTER(Enum):
        USER = "USER"

    @abstractmethod
    async def list(self, filter: Dict[FILTER, Any] = None) -> List[Campaign]:
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
    class FILTER(Enum):
        USER = "USER"
        CAMPAIGN = "CAMPAIGN"
        PARTY = "PARTY"

    @abstractmethod
    async def list(self, filter: Dict[FILTER, Any] = None) -> List[PlayerCharacter]:
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


class BasePartyStorage(BaseStorage):
    class FILTER(Enum):
        CAMPAIGN = "CAMPAIGN"
        PLAYER_CHARACTER = "PLAYER_CHARACTER"

    @abstractmethod
    async def list(self, filter: Dict[FILTER, Any] = None) -> List[Party]:
        raise NotImplementedError

    @abstractmethod
    async def get(self, uuid: UUID4) -> Optional[Party]:
        raise NotImplementedError

    @abstractmethod
    async def save(self, entity: Party):
        raise NotImplementedError

    @abstractmethod
    async def remove_player_character(self, uuid: UUID4, player_character_id: UUID4):
        raise NotImplementedError

    @abstractmethod
    async def save_all(self, entities: List[Party]):
        raise NotImplementedError


async def seed_party(
    storage: BasePartyStorage,
    campaign: Campaign,
    player_characters: list[PlayerCharacter],
):
    party = mock_party(campaign, player_characters)
    await storage.save(party)
    return party
