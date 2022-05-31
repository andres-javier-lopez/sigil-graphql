import logging
from typing import List, Optional

from pydantic import UUID4
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from sigil.domain.entities import Hub
from sigil.storage.adapters.psql import select
from sigil.storage.adapters.psql.models import HubModel
from sigil.storage.domain.town import BaseHubStorage

logger = logging.getLogger(__name__)


class HubStorage(BaseHubStorage):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def list(self, filter: dict = None) -> List[Hub]:
        stmt = select(HubModel)
        if filter:
            filter_func = {
                self.FILTER.CAMPAIGN: lambda v: HubModel.campaign_id == v,
            }

            stmt = stmt.filter(
                *[filter_func[keyword](value) for keyword, value in filter.items()]
            )
        logger.info(stmt)
        result: Result = await self.session.execute(stmt)
        rows = result.scalars()
        if rows:
            hubs = [row.get_entity() for row in rows]
            return hubs

        return []

    async def get(self, uuid: UUID4) -> Optional[Hub]:
        model: HubModel = await self.session.get(HubModel, uuid)
        if model:
            return model.get_entity()

        return None

    async def save(self, entity: Hub, autoflush=True):
        model: HubModel = await self.session.get(HubModel, entity.uuid)
        if model is None:
            model = HubModel.from_entity(entity)
            self.session.add(model)
        else:
            model.set_entity(entity)
        if autoflush:
            await self.session.flush()

    async def save_all(self, entities: List[Hub]):
        for entity in entities:
            await self.save(entity, autoflush=False)
        await self.session.flush()

    async def delete(self, uuid: UUID4):
        model = await self.session.get(HubModel, uuid)
        await self.session.delete(model)
        await self.session.flush()
