from fastapi import FastAPI

from . import __version__
from .graphql.app import app as graphql_app


app = FastAPI(title='Sigil', version=__version__)
app.mount('/graphql', graphql_app)
