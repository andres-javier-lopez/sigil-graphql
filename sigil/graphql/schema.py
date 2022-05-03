from os import path

from ariadne import (
    load_schema_from_path,
    make_executable_schema,
    snake_case_fallback_resolvers,
)

from sigil.domain.campaign import schema as campaign
from sigil.domain.town import schema as town

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
    campaign.campaign_type,
    snake_case_fallback_resolvers,
)
