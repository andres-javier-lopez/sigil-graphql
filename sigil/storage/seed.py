from sigil.storage.domain.campaign import (
    seed_campaigns,
    seed_party,
    seed_player_characters,
)
from sigil.storage.domain.town import seed_hubs
from sigil.storage.interfaces import StorageManager


async def seed():
    async with StorageManager.start() as storages:
        campaigns = await seed_campaigns(storages.campaign_storage, number=3)
        for campaign in campaigns:
            player_characters = await seed_player_characters(
                storages.player_character_storage, campaign, number=4
            )
            await seed_party(storages.party_storage, campaign, player_characters)
            await seed_hubs(storages.hub_storage, campaign)
