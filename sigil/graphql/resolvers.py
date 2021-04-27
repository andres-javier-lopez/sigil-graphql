from ariadne import QueryType

from sigil import __version__


query = QueryType()


@query.field('version')
async def version_resolver(*_):
    return __version__
