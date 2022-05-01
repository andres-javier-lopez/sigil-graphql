"""Use cases for campaign module"""

from uuid import UUID

from sigil.storage.interfaces import CampaignStorage, PlayerCharacterStorage


class CampaignManager:
    def __init__(self, storage: CampaignStorage, user_id: UUID = None):
        self.storage = storage
        self.user_id = user_id

    async def list_all(self):
        campaigns = await self.storage.list(filter={"user_id": self.user_id})
        return campaigns


class PlayerCharacterManager:
    def __init__(self, storage: PlayerCharacterStorage, user_id: UUID = None):
        self.storage = storage
        self.user_id = user_id

    async def list_all(self):
        player_characters = await self.storage.list(filter={"user_id": self.user_id})
        return player_characters

    async def list_from_campaign(self, campaign):
        player_characters = await self.storage.list(
            filter={"campaign_id": campaign.uuid}
        )
        return player_characters
