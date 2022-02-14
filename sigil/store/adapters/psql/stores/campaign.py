from typing import List, Optional

from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from sigil.domain.campaign.entities import Campaign
from sigil.store.adapters.psql import select
from sigil.store.adapters.psql.models import CampaignModel
from sigil.store.campaign.base import BaseCampaignStore


class CampaingStorePsql(BaseCampaignStore):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def list(self) -> List[Campaign]:
        stmt = select(CampaignModel)
        result = await self.session.execute(stmt)
        campaings = [
            Campaign.from_orm(row) for row in result.scalars()
        ]
        return campaings

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
