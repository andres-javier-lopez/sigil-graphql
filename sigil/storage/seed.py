from sigil.storage.adapters.psql.commands import include_storages
from sigil.storage.domain.campaign import (
    seed_campaigns,
    seed_party,
    seed_player_characters,
)
from sigil.storage.interfaces import (
    CampaignStorage,
    PartyStorage,
    PlayerCharacterStorage,
)


@include_storages
async def seed(*, storages: dict = None):
    campaigns = await seed_campaigns(storages[CampaignStorage.__name__], number=3)
    for campaign in campaigns:
        player_characters = await seed_player_characters(
            storages[PlayerCharacterStorage.__name__], campaign, number=4
        )
        await seed_party(storages[PartyStorage.__name__], campaign, player_characters)
