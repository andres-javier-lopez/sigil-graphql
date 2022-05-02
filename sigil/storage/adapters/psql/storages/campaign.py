import logging
from typing import List, Optional

from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from sigil.domain.campaign.entities import Campaign, PlayerCharacter
from sigil.storage.adapters.psql import delete, select
from sigil.storage.adapters.psql.models import CampaignModel, PlayerCharacterModel
from sigil.storage.adapters.psql.models.campaign import Character, RelationshipModel
from sigil.storage.domain.campaign import (
    BaseCampaignStorage,
    BasePlayerCharacterStorage,
)

logger = logging.getLogger(__name__)


class CampaignStoragePsql(BaseCampaignStorage):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def list(self, filter: dict = None) -> List[Campaign]:
        stmt = select(CampaignModel)
        if filter:
            stmt = stmt.filter_by(**filter)
        logger.info(stmt)
        result = await self.session.execute(stmt)
        campaigns = [Campaign.from_orm(row) for row in result.scalars()]
        return campaigns

    async def get(self, uuid: UUID4) -> Optional[Campaign]:
        result = await self.session.get(CampaignModel, uuid)
        if result:
            return Campaign.from_orm(result)

        return None

    async def save(self, entity: Campaign):
        model: CampaignModel = await self.session.get(CampaignModel, entity.uuid)
        if model is None:
            model = CampaignModel.from_entity(entity)
        else:
            model.set_entity(entity)
        self.session.add(model)
        await self.session.flush()

    async def save_all(self, entities: List[Campaign]):
        for entity in entities:
            await self.save(entity)

    async def delete(self, uuid: UUID4):
        model = await self.session.get(CampaignModel, uuid)
        await self.session.delete(model)


class PlayerCharacterStoragePsql(BasePlayerCharacterStorage):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def list(self, filter: dict = None) -> List[PlayerCharacter]:
        stmt = select(PlayerCharacterModel)
        if filter:
            stmt = stmt.filter_by(**filter)
        logger.info(stmt)
        result = await self.session.execute(stmt)
        player_characters = [PlayerCharacter.from_orm(row) for row in result.scalars()]
        return player_characters

    async def get(self, uuid: UUID4) -> Optional[PlayerCharacter]:
        result = await self.session.get(PlayerCharacterModel, uuid)
        if result:
            return PlayerCharacter.from_orm(result)

        return None

    async def save(self, entity: PlayerCharacter):
        model: PlayerCharacterModel = await self.session.get(
            PlayerCharacterModel, entity.uuid
        )
        if model is None:
            model = PlayerCharacterModel.from_entity(entity)
        else:
            model.set_entity(entity)
        self.session.add(model)
        await self.session.flush()

        await self.add_update_relationships(entity)

    async def add_update_relationships(self, entity: PlayerCharacter):
        """Add new relationship or update existing ones.

        We don't delete relationships here because the relationship list doesn't
        have to be up to date in the entity.
        """
        stmt = select(RelationshipModel).filter(
            RelationshipModel.player_character_id == entity.uuid
        )
        result = await self.session.execute(stmt)

        relationship_data = {re.character.uuid: re for re in entity.relationships}

        # Update existing relationship
        for relationship in result.scalars():
            character_uuid = relationship.character_id
            if character_uuid in relationship_data:
                relationship.status = relationship_data[character_uuid].status
                relationship.notes = relationship_data[character_uuid].notes
                del relationship_data[character_uuid]

        if relationship_data:  # There are new relationships leftover
            for uuid, relationship in relationship_data.items():
                if isinstance(relationship.character, PlayerCharacter):
                    character_entity = Character.PlayerCharacter
                else:
                    raise ValueError(
                        f"{relationship.character.__class__} is not a valid character"
                    )
                relationship_model = RelationshipModel(
                    player_character_id=entity.uuid,
                    character_id=uuid,
                    character_entity=character_entity,
                    status=relationship.status,
                    notes=relationship.notes,
                )
                self.session.add(relationship_model)

        await self.session.flush()

    async def delete_relationship(
        self, player_character_id: UUID4, character_id: UUID4
    ):
        stmt = delete(RelationshipModel).where(
            RelationshipModel.player_character_id == player_character_id,
            RelationshipModel.character_id == character_id,
        )
        logger.info(stmt)
        await self.session.execute(stmt)

    async def save_all(self, entities: List[PlayerCharacter]):
        for entity in entities:
            await self.save(entity)

    async def delete(self, uuid: UUID4):
        model = await self.session.get(PlayerCharacterModel, uuid)
        await self.session.delete(model)
