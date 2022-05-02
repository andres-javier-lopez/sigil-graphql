import logging

from sqlalchemy.ext.asyncio import AsyncSession

from sigil.domain.campaign.entities import PlayerCharacter
from sigil.domain.town.entities.base import Relationship
from sigil.storage.adapters.psql import select
from sigil.storage.adapters.psql.models.campaign import (
    Character,
    PlayerCharacterModel,
    RelationshipModel,
)

logger = logging.getLogger(__name__)


class RelationshipStoragePsql:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def list_player_character_relationships(
        self,
        player_character: PlayerCharacter,
    ) -> list[Relationship]:
        stmt = select(RelationshipModel).filter(
            RelationshipModel.player_character_id == player_character.uuid
        )
        logger.info(stmt)
        results = await self.session.execute(stmt)

        relationships = []
        for relationship in results.scalars():
            if relationship.character_entity == Character.PlayerCharacter:
                # This is not very efficient
                result = await self.session.get(
                    PlayerCharacterModel, relationship.character_id
                )
                if result:
                    character = PlayerCharacter.from_orm(result)

            relationships.append(
                Relationship(
                    character=character,
                    status=relationship.status,
                    notes=relationship.notes,
                )
            )

        return relationships
