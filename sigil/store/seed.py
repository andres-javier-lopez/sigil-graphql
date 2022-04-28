from sigil.store.adapters.psql.seed import seed_stores
from sigil.store.domain.campaign import seed_campaigns
from sigil.store.interfaces import CampaignStore


@seed_stores
async def seed(*, stores: dict = None):
    await seed_campaigns(stores[CampaignStore.__name__], number=5)
