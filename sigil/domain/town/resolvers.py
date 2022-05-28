from graphql import GraphQLResolveInfo

from sigil.auth.utils import get_user_id
from sigil.domain.entities import Campaign
from sigil.domain.town.actions import HubManager
from sigil.graphql.utils import get_request
from sigil.storage.interfaces import StorageManager


async def campaign_hubs_resolver(campaign: Campaign, info: GraphQLResolveInfo):
    request = get_request(info)
    user_id = get_user_id(request)

    async with StorageManager.start() as storages:
        manager = HubManager(storages.hub_storage, user_id=user_id)

        return await manager.list_for_campaign(campaign)
