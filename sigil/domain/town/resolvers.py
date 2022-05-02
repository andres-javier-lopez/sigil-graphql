from typing import Union

from graphql import GraphQLResolveInfo
from sigil.auth.utils import get_user_id
from sigil.domain.campaign.entities import PlayerCharacter
from sigil.domain.town.actions import RelationshipManager
from sigil.domain.town.entities.base import NPC
from sigil.graphql.utils import get_request
from sigil.storage.adapters.psql import async_session
from sigil.storage.interfaces import RelationshipStorage


async def player_character_relationship_resolver(
    player_character: PlayerCharacter, info: GraphQLResolveInfo
):
    request = get_request(info)
    user_id = get_user_id(request)

    async with async_session() as session:
        storage = RelationshipStorage(session)
        manager = RelationshipManager(storage, user_id)

        return await manager.list_player_character_relationships(player_character)


async def character_union_resolver(character: Union[PlayerCharacter, NPC], *_):
    return character.__class__.__name__
