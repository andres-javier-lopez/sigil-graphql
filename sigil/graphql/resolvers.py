import logging

from ariadne import QueryType

from sigil import __version__
from sigil.domain.campaign.resolvers import (
    campaigns_resolver,
    player_character_resolver,
)

logger = logging.getLogger(__name__)

query = QueryType()


@query.field("version")
async def version_resolver(*_):
    return __version__


query.set_field("campaigns", campaigns_resolver)
query.set_field("playerCharacters", player_character_resolver)
