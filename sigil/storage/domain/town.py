from abc import abstractmethod
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import UUID4

from sigil.domain.entities import Campaign, Hub
from sigil.domain.mocks import mock_hubs
from sigil.storage.base import BaseStorage


class BaseHubStorage(BaseStorage):
    class FILTER(Enum):
        CAMPAIGN = "CAMPAIGN"

    @abstractmethod
    async def list(self, filter: Dict[FILTER, Any] = None) -> List[Hub]:
        raise NotImplementedError

    @abstractmethod
    async def get(self, uuid: UUID4) -> Optional[Hub]:
        raise NotImplementedError

    @abstractmethod
    async def save(self, entity: Hub):
        raise NotImplementedError

    @abstractmethod
    async def save_all(self, entities: List[Hub]):
        raise NotImplementedError


async def seed_hubs(storage: BaseHubStorage, campaign: Campaign, number=2) -> List[Hub]:
    hubs = mock_hubs(campaign, number)
    storage.save_all(hubs)
    return hubs
