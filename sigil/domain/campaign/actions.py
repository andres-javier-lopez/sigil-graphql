"""Use cases for campaign module"""

from uuid import UUID

from sigil.storage.interfaces import CampaignStorage


class CampaignManager:
    def __init__(self, storage: CampaignStorage, user_id: UUID = None):
        self.storage = storage
        self.user_id = user_id

    async def list_all(self):
        campaigns = await self.storage.list(filter={"user_id": self.user_id})
        return campaigns
