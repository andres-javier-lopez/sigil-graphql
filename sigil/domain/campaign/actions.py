"""Use cases for campaign module"""

from uuid import UUID

from sigil.domain.entities import Campaign, Party, PlayerCharacter
from sigil.storage.interfaces import (
    CampaignStorage,
    PartyStorage,
    PlayerCharacterStorage,
)


class CampaignManager:
    def __init__(self, storage: CampaignStorage, user_id: UUID = None):
        self.storage = storage
        self.user_id = user_id

    async def list_all(self) -> list[Campaign]:
        campaigns = await self.storage.list(
            filter={self.storage.FILTER.USER: self.user_id}
        )
        return campaigns


class PlayerCharacterManager:
    def __init__(self, storage: PlayerCharacterStorage, user_id: UUID = None):
        self.storage = storage
        self.user_id = user_id

    async def list_all(self) -> list[PlayerCharacter]:
        player_characters = await self.storage.list(
            filter={self.storage.FILTER.USER: self.user_id}
        )
        return player_characters

    async def list_for_campaign(self, campaign: Campaign) -> list[PlayerCharacter]:
        player_characters = await self.storage.list(
            filter={self.storage.FILTER.CAMPAIGN: campaign.uuid}
        )
        return player_characters

    async def list_for_party(self, party: Party) -> list[PlayerCharacter]:
        player_characters = await self.storage.list(
            filter={self.storage.FILTER.PARTY: party.uuid}
        )
        return player_characters


class PartyManager:
    def __init__(self, storage: PartyStorage, user_id: UUID = None):
        self.storage = storage
        self.user_id = user_id

    async def list_for_campaign(self, campaign: Campaign) -> list[Party]:
        parties = await self.storage.list(
            filter={self.storage.FILTER.CAMPAIGN: campaign.uuid}
        )
        return parties

    async def list_for_player(self, player_character: PlayerCharacter) -> list[Party]:
        parties = await self.storage.list(
            filter={self.storage.FILTER.PLAYER_CHARACTER: player_character.uuid}
        )
        return parties
