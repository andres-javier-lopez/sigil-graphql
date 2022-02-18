"""Use cases for campaign module"""

from sigil.store.interfaces import CampaignStore


class CampaignManager:
    def __init__(self, store: CampaignStore):
        self.store = store

    async def list_all(self):
        campaigns = await self.store.list()
        return campaigns
