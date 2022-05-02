from uuid import UUID

from sigil.domain.campaign.entities import PlayerCharacter
from sigil.storage.interfaces import RelationshipStorage


class RelationshipManager:
    def __init__(self, storage: RelationshipStorage, user_id: UUID = None):
        self.storage = storage
        self.user_id = user_id

    async def list_player_character_relationships(
        self, player_character: PlayerCharacter
    ):
        return await self.storage.list_player_character_relationships(player_character)
