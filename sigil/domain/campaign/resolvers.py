from sigil.domain.campaign.actions import CampaignManager
from sigil.storage.adapters.psql import async_session
from sigil.storage.interfaces import CampaignStorage


async def campaigns_resolver(*_):
    async with async_session() as session:
        storage = CampaignStorage(session)
        manager = CampaignManager(storage)

        return await manager.list_all()
