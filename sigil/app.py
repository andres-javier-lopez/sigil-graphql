import ariadne
from ariadne.asgi import GraphQL
from fastapi import FastAPI

from . import __version__


type_defs = """
    type Query {
        hello: String!
    }
"""

schema = ariadne.make_executable_schema(type_defs)

graphql_app = GraphQL(schema)


app = FastAPI(title='Sigil', version=__version__)
app.mount('/graphql', graphql_app)
