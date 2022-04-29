from os import path

from ariadne import load_schema_from_path

basepath = path.dirname(__file__)
schemapath = path.abspath(path.join(basepath, "schemas"))


type_defs = load_schema_from_path(schemapath)
