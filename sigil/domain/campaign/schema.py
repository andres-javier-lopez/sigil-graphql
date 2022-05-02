from os import path

from ariadne import ObjectType, load_schema_from_path

from .resolvers import campaign_player_characters_resolver

basepath = path.dirname(__file__)
schemapath = path.abspath(path.join(basepath, "schemas"))


type_defs = load_schema_from_path(schemapath)

campaign_type = ObjectType("Campaign")
campaign_type.set_field("playerCharacters", campaign_player_characters_resolver)
