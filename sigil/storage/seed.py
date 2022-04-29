from sigil.storage.adapters.psql.commands import include_storages
from sigil.storage.domain.campaign import seed_campaigns
from sigil.storage.interfaces import CampaignStorage


@include_storages
async def seed(*, storages: dict = None):
    await seed_campaigns(storages[CampaignStorage.__name__], number=5)
