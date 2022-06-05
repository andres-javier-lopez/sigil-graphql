from graphql import GraphQLResolveInfo

from sigil.auth.utils import get_user_id
from sigil.domain.campaign.actions import (
    CampaignManager,
    PartyManager,
    PlayerCharacterManager,
)
from sigil.domain.entities import Campaign, Party, PlayerCharacter
from sigil.graphql.utils import get_request
from sigil.storage.manager import StorageManager


async def campaigns_resolver(_, info: GraphQLResolveInfo):
    request = get_request(info)
    user_id = get_user_id(request)

    async with StorageManager.load() as storages:
        manager = CampaignManager(storages.campaign_storage, user_id=user_id)

        return await manager.list_all()


async def campaign_player_characters_resolver(
    campaign: Campaign, info: GraphQLResolveInfo
):
    request = get_request(info)
    user_id = get_user_id(request)

    async with StorageManager.load() as storages:
        manager = PlayerCharacterManager(
            storages.player_character_storage, user_id=user_id
        )

        return await manager.list_for_campaign(campaign)


async def campaign_parties_resolver(campaign: Campaign, info: GraphQLResolveInfo):
    request = get_request(info)
    user_id = get_user_id(request)

    async with StorageManager.load() as storages:
        manager = PartyManager(storages.party_storage, user_id=user_id)

        return await manager.list_for_campaign(campaign)


async def player_character_resolver(_, info: GraphQLResolveInfo):
    request = get_request(info)
    user_id = get_user_id(request)

    async with StorageManager.load() as storages:
        manager = PlayerCharacterManager(
            storages.player_character_storage, user_id=user_id
        )

        return await manager.list_all()


async def player_character_parties_resolver(
    player_character: PlayerCharacter, info: GraphQLResolveInfo
):
    request = get_request(info)
    user_id = get_user_id(request)

    async with StorageManager.load() as storages:
        manager = PartyManager(storages.party_storage, user_id=user_id)

        return await manager.list_for_player(player_character)


async def party_player_characters_resolver(party: Party, info: GraphQLResolveInfo):
    request = get_request(info)
    user_id = get_user_id(request)

    async with StorageManager.load() as storages:
        manager = PlayerCharacterManager(
            storages.player_character_storage, user_id=user_id
        )

        return await manager.list_for_party(party)
