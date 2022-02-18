from abc import abstractmethod
from typing import List, Optional

from pydantic import UUID4

from sigil.domain.campaign.entities import Campaign
from sigil.domain.campaign.entities.mocks import mock_campaigns
from sigil.store.base import BaseStore


class BaseCampaignStore(BaseStore):
    @abstractmethod
    async def list(self) -> List[Campaign]:
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


async def seed_campaigns(store: BaseCampaignStore, number=5):
    campaigns = mock_campaigns(number=number)
    await store.save_all(campaigns)