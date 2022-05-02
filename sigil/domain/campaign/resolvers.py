from ariadne import ObjectType

from graphql import GraphQLResolveInfo
from sigil.auth.utils import get_user_id
from sigil.domain.campaign.actions import CampaignManager, PlayerCharacterManager
from sigil.domain.town.resolvers import player_character_relationship_resolver
from sigil.graphql.utils import get_request
from sigil.storage.adapters.psql import async_session
from sigil.storage.interfaces import CampaignStorage, PlayerCharacterStorage

campaign_type = ObjectType("Campaign")
player_character_type = ObjectType("PlayerCharacter")

player_character_type.set_field("relationships", player_character_relationship_resolver)


async def campaigns_resolver(_, info: GraphQLResolveInfo):
    request = get_request(info)
    user_id = get_user_id(request)

    async with async_session() as session:
        storage = CampaignStorage(session)
        manager = CampaignManager(storage, user_id=user_id)

        return await manager.list_all()


@campaign_type.field("playerCharacters")
async def campaign_player_characters_resolver(campaign, info: GraphQLResolveInfo):
    request = get_request(info)
    user_id = get_user_id(request)

    async with async_session() as session:
        storage = PlayerCharacterStorage(session)
        manager = PlayerCharacterManager(storage, user_id=user_id)

        return await manager.list_from_campaign(campaign)


async def player_character_resolver(_, info: GraphQLResolveInfo):
    request = get_request(info)
    user_id = get_user_id(request)

    async with async_session() as session:
        storage = PlayerCharacterStorage(session)
        manager = PlayerCharacterManager(storage, user_id=user_id)

        return await manager.list_all()
