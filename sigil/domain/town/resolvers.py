from graphql import GraphQLResolveInfo

from sigil.auth.utils import get_user_id
from sigil.domain.entities import Campaign
from sigil.domain.town.actions import HubManager
from sigil.graphql.utils import get_request
from sigil.storage.adapters.psql import async_session
from sigil.storage.interfaces import HubStorage


async def campaign_hubs_resolver(campaign: Campaign, info: GraphQLResolveInfo):
    request = get_request(info)
    user_id = get_user_id(request)

    async with async_session() as session:
        storage = HubStorage(session)
        manager = HubManager(storage, user_id=user_id)

        return await manager.list_for_campaign(campaign)
