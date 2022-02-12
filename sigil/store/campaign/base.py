from abc import abstractmethod
from typing import List, Optional

from pydantic import UUID4

from ..base import BaseStore
from sigil.domain.campaign.entities import Campaign


class CampaignStore(BaseStore):
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
