from sigil.store.adapters.psql.commands import include_storages
from sigil.store.domain.campaign import seed_campaigns
from sigil.store.interfaces import CampaignStore


@include_storages
async def seed(*, stores: dict = None):
    await seed_campaigns(stores[CampaignStore.__name__], number=5)
