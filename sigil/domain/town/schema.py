from os import path

from ariadne import UnionType, load_schema_from_path

from .resolvers import character_union_resolver

basepath = path.dirname(__file__)
schemapath = path.abspath(path.join(basepath, "schemas"))


type_defs = load_schema_from_path(schemapath)

character_union = UnionType("Character", character_union_resolver)
