from os import path

from ariadne import ObjectType, load_schema_from_path

from .resolvers import (
    campaign_parties_resolver,
    campaign_player_characters_resolver,
    party_player_characters_resolver,
    player_character_parties_resolver,
)

basepath = path.dirname(__file__)
schemapath = path.abspath(path.join(basepath, "schemas"))


type_defs = load_schema_from_path(schemapath)

campaign_type = ObjectType("Campaign")
campaign_type.set_field("playerCharacters", campaign_player_characters_resolver)
campaign_type.set_field("parties", campaign_parties_resolver)

player_character_type = ObjectType("PlayerCharacter")
player_character_type.set_field("parties", player_character_parties_resolver)

party_type = ObjectType("Party")
party_type.set_field("playerCharacters", party_player_characters_resolver)

object_types = [campaign_type, player_character_type, party_type]
