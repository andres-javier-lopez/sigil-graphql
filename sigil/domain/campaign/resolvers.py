from sigil.domain.campaign.actions import CampaignManager
from sigil.store.adapters.psql import async_session
from sigil.store.interfaces import CampaignStore


async def campaigns_resolver(*_):
    async with async_session() as session:
        store = CampaignStore(session)
        manager = CampaignManager(store)

        return await manager.list_all()
