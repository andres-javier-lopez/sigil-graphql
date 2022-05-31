from uuid import UUID

from sigil.domain.entities import Campaign, Hub
from sigil.storage.interfaces import HubStorage


class HubManager:
    def __init__(self, storage: HubStorage, user_id: UUID = None):
        self.storage = storage
        self.user_id = user_id

    async def list_for_campaign(self, campaign: Campaign) -> list[Hub]:
        hubs = await self.storage.list(
            filter={self.storage.FILTER.CAMPAIGN: campaign.uuid}
        )
        return hubs
