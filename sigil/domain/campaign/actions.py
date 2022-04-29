"""Use cases for campaign module"""

from sigil.storage.interfaces import CampaignStorage


class CampaignManager:
    def __init__(self, storage: CampaignStorage):
        self.storage = storage

    async def list_all(self):
        campaigns = await self.storage.list()
        return campaigns
