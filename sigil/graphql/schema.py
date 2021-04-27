from os import path

from ariadne import load_schema_from_path, make_executable_schema

from .resolvers import query


basepath = path.dirname(__file__)
schemapath = path.abspath(path.join(basepath, 'schemas'))

type_defs = load_schema_from_path(schemapath)


schema = make_executable_schema(
    [
        type_defs,
    ],
    query,
)
