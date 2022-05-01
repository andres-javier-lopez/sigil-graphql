import logging
from typing import List, Optional

from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from sigil.domain.campaign.entities import Campaign, PlayerCharacter
from sigil.storage.adapters.psql import select
from sigil.storage.adapters.psql.models import CampaignModel, PlayerCharacterModel
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
        logger.info(f"saving {entity}")
        model: PlayerCharacterModel = await self.session.get(
            PlayerCharacterModel, entity.uuid
        )
        if model is None:
            model = PlayerCharacterModel.from_entity(entity)
        else:
            model.set_entity(entity)
        self.session.add(model)
        await self.session.flush()

    async def save_all(self, entities: List[PlayerCharacter]):
        for entity in entities:
            await self.save(entity)

    async def delete(self, uuid: UUID4):
        model = await self.session.get(PlayerCharacterModel, uuid)
        await self.session.delete(model)
