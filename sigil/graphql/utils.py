from starlette.requests import Request

from graphql import GraphQLResolveInfo


def get_request(info: GraphQLResolveInfo) -> Request:
    request = info.context["request"]
    return request
