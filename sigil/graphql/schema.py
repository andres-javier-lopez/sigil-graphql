from os import path

from ariadne import (
    load_schema_from_path,
    make_executable_schema,
    snake_case_fallback_resolvers,
)

from sigil.domain import campaign, town
from sigil.domain.campaign.resolvers import campaign_type, player_character_type

from .resolvers import query

basepath = path.dirname(__file__)
schemapath = path.abspath(path.join(basepath, "schemas"))

type_defs = load_schema_from_path(schemapath)


schema = make_executable_schema(
    [
        type_defs,
        campaign.type_defs,
        town.type_defs,
    ],
    query,
    campaign_type,
    player_character_type,
    town.character_union,
    snake_case_fallback_resolvers,
)
