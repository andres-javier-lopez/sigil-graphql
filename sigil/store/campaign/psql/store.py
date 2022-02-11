from typing import List, Optional

from pydantic import UUID4

from ..base import CampaignStore
from sigil.domain.campaign.entities import Campaign


class CampaingStorePsql(CampaignStore):
    async def list(self) -> List[Campaign]:
        return []

    async def get(self, uuid: UUID4) -> Optional[Campaign]:
        return None

    async def save(self, model: Campaign):
        ...

    async def save_all(self, models: List[Campaign]):
        ...

    async def delete(self, uuid: UUID4):
        ...
