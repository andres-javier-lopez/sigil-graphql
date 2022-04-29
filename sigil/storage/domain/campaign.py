from abc import abstractmethod
from typing import List, Optional

from pydantic import UUID4

from sigil.domain.campaign.entities import Campaign
from sigil.domain.campaign.entities.mocks import mock_campaigns
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

    @abstractmethod
    async def delete(self, uuid: UUID4):
        raise NotImplementedError


async def seed_campaigns(storage: BaseCampaignStorage, number=5):
    campaigns = mock_campaigns(number=number)
    await storage.save_all(campaigns)
