import graphene

import hackernews.links.schemas as link_schema


class Query(link_schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
