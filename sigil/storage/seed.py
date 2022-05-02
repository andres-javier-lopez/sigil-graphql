from sigil.storage.adapters.psql.commands import include_storages
from sigil.storage.domain.campaign import seed_campaigns, seed_player_characters
from sigil.storage.interfaces import CampaignStorage, PlayerCharacterStorage


@include_storages
async def seed(*, storages: dict = None):
    campaigns = await seed_campaigns(storages[CampaignStorage.__name__], number=3)
    for campaign in campaigns:
        await seed_player_characters(
            storages[PlayerCharacterStorage.__name__], campaign, number=4
        )
