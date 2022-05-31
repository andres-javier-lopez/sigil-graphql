from os import path

from ariadne import load_schema_from_path

from sigil.domain.campaign.schema import campaign_type

from .resolvers import campaign_hubs_resolver

basepath = path.dirname(__file__)
schemapath = path.abspath(path.join(basepath, "schemas"))


type_defs = load_schema_from_path(schemapath)

campaign_type.set_field("hubs", campaign_hubs_resolver)
