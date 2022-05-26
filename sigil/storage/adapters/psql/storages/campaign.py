import logging
from typing import List, Optional

from pydantic import UUID4
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from sigil.domain.entities import Campaign, Party, PlayerCharacter
from sigil.storage.adapters.psql import select
from sigil.storage.adapters.psql.models import (
    CampaignModel,
    PartyModel,
    PlayerCharacterModel,
)
from sigil.storage.domain.campaign import (
    BaseCampaignStorage,
    BasePartyStorage,
    BasePlayerCharacterStorage,
)

logger = logging.getLogger(__name__)


class CampaignStorage(BaseCampaignStorage):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def list(self, filter: dict = None) -> List[Campaign]:
        stmt = select(CampaignModel)
        if filter:
            filter_func = {
                self.FILTER.USER: lambda v: CampaignModel.user_id == v,
            }

            stmt = stmt.filter(
                *[filter_func[keyword](value) for keyword, value in filter.items()]
            )
        logger.info(stmt)
        result: Result = await self.session.execute(stmt)
        rows = result.scalars()
        if rows:
            campaigns = [row.get_entity() for row in rows]
            return campaigns

        return []

    async def get(self, uuid: UUID4) -> Optional[Campaign]:
        model: CampaignModel = await self.session.get(CampaignModel, uuid)
        if model:
            return model.get_entity()

        return None

    async def save(self, entity: Campaign, autoflush=True):
        model: CampaignModel = await self.session.get(CampaignModel, entity.uuid)
        if model is None:
            model = CampaignModel.from_entity(entity)
            self.session.add(model)
        else:
            model.set_entity(entity)
        if autoflush:
            await self.session.flush()

    async def save_all(self, entities: List[Campaign]):
        for entity in entities:
            await self.save(entity, autoflush=False)
        await self.session.flush()

    async def delete(self, uuid: UUID4):
        model = await self.session.get(CampaignModel, uuid)
        await self.session.delete(model)
        await self.session.flush()


class PlayerCharacterStorage(BasePlayerCharacterStorage):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def list(self, filter: dict = None) -> List[PlayerCharacter]:
        stmt = select(PlayerCharacterModel)
        if filter:
            filter_func = {
                self.FILTER.USER: lambda v: PlayerCharacterModel.user_id == v,
                self.FILTER.CAMPAIGN: lambda v: PlayerCharacterModel.campaign_id == v,
                self.FILTER.PARTY: lambda v: PlayerCharacterModel.parties.any(
                    PartyModel.uuid == v
                ),
            }

            stmt = stmt.filter(
                *[filter_func[keyword](value) for keyword, value in filter.items()]
            )
        logger.info(stmt)
        result: Result = await self.session.execute(stmt)
        rows = result.scalars()
        if rows:
            player_characters = [row.get_entity() for row in rows]
            return player_characters

        return []

    async def get(self, uuid: UUID4) -> Optional[PlayerCharacter]:
        model: PlayerCharacterModel = await self.session.get(PlayerCharacterModel, uuid)
        if model:
            return model.get_entity()

        return None

    async def save(self, entity: PlayerCharacter, autoflush=True):
        model: PlayerCharacterModel = await self.session.get(
            PlayerCharacterModel, entity.uuid
        )
        if model is None:
            model = PlayerCharacterModel.from_entity(entity)
            self.session.add(model)
        else:
            model.set_entity(entity)
        if autoflush:
            await self.session.flush()

    async def save_all(self, entities: List[PlayerCharacter]):
        for entity in entities:
            await self.save(entity, autoflush=False)
        await self.session.flush()

    async def delete(self, uuid: UUID4):
        model = await self.session.get(PlayerCharacterModel, uuid)
        await self.session.delete(model)
        await self.session.flush()


class PartyStorage(BasePartyStorage):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def list(self, filter: dict = None) -> List[Party]:
        stmt = select(PartyModel)
        if filter:
            filter_func = {
                self.FILTER.CAMPAIGN: lambda v: PartyModel.campaign_id == v,
                self.FILTER.PLAYER_CHARACTER: lambda v: (
                    PartyModel.player_characters.any(PlayerCharacterModel.uuid == v)
                ),
            }

            stmt = stmt.filter(
                *[filter_func[keyword](value) for keyword, value in filter.items()]
            )
        logger.info(stmt)
        result: Result = await self.session.execute(stmt)
        rows = result.scalars()
        if rows:
            parties = [row.get_entity() for row in rows]
            return parties

        return []

    async def get(self, uuid: UUID4) -> Optional[Party]:
        model: PartyModel = await self.session.get(PartyModel, uuid)
        if model:
            return model.get_entity()

        return None

    async def save(self, entity: Party, autoflush=True):
        model: PartyModel = await self.session.get(PartyModel, entity.uuid)
        if model is None:
            model = PartyModel.from_entity(entity)
            self.session.add(model)
        else:
            model.set_entity(entity)

        for player_character in entity.player_characters:
            player_character_model = await self.session.get(
                PlayerCharacterModel, player_character.uuid
            )
            if player_character_model:
                model.player_characters.append(player_character_model)
            else:
                logger.warning(
                    f"Tried to add unsaved character {player_character.uuid} "
                    f"to party {entity.uuid}"
                )

        if autoflush:
            await self.session.flush()

    async def remove_player_character(self, uuid: UUID4, player_character_id: UUID4):
        party_model: PartyModel = await self.session.get(PartyModel, uuid)
        player_character_model = await self.session.get(
            PlayerCharacterModel, player_character_id
        )
        party_model.player_characters.remove(player_character_model)
        await self.session.flush()

    async def save_all(self, entities: List[Party]):
        for entity in entities:
            await self.save(entity, autoflush=False)
        await self.session.flush()

    async def delete(self, uuid: UUID4):
        model = await self.session.get(PartyModel, uuid)
        await self.session.delete(model)
        await self.session.flush()
