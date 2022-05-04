from graphql import GraphQLResolveInfo

from sigil.auth.utils import get_user_id
from sigil.domain.campaign.actions import (
    CampaignManager,
    PartyManager,
    PlayerCharacterManager,
)
from sigil.domain.entities import Campaign, Party, PlayerCharacter
from sigil.graphql.utils import get_request
from sigil.storage.adapters.psql import async_session
from sigil.storage.interfaces import (
    CampaignStorage,
    PartyStorage,
    PlayerCharacterStorage,
)


async def campaigns_resolver(_, info: GraphQLResolveInfo):
    request = get_request(info)
    user_id = get_user_id(request)

    async with async_session() as session:
        storage = CampaignStorage(session)
        manager = CampaignManager(storage, user_id=user_id)

        return await manager.list_all()


async def campaign_player_characters_resolver(
    campaign: Campaign, info: GraphQLResolveInfo
):
    request = get_request(info)
    user_id = get_user_id(request)

    async with async_session() as session:
        storage = PlayerCharacterStorage(session)
        manager = PlayerCharacterManager(storage, user_id=user_id)

        return await manager.list_for_campaign(campaign)


async def campaign_parties_resolver(campaign: Campaign, info: GraphQLResolveInfo):
    request = get_request(info)
    user_id = get_user_id(request)

    async with async_session() as session:
        storage = PartyStorage(session)
        manager = PartyManager(storage, user_id=user_id)

        return await manager.list_for_campaign(campaign)


async def player_character_resolver(_, info: GraphQLResolveInfo):
    request = get_request(info)
    user_id = get_user_id(request)

    async with async_session() as session:
        storage = PlayerCharacterStorage(session)
        manager = PlayerCharacterManager(storage, user_id=user_id)

        return await manager.list_all()


async def player_character_parties_resolver(
    player_character: PlayerCharacter, info: GraphQLResolveInfo
):
    request = get_request(info)
    user_id = get_user_id(request)

    async with async_session() as session:
        storage = PartyStorage(session)
        manager = PartyManager(storage, user_id)

        return await manager.list_for_player(player_character)


async def party_player_characters_resolver(party: Party, info: GraphQLResolveInfo):
    request = get_request(info)
    user_id = get_user_id(request)

    async with async_session() as session:
        storage = PlayerCharacterStorage(session)
        manager = PlayerCharacterManager(storage, user_id)

        return await manager.list_for_party(party)
