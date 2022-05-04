from graphql import GraphQLResolveInfo
from starlette.requests import Request


def get_request(info: GraphQLResolveInfo) -> Request:
    request = info.context["request"]
    return request
