import graphene

import links.schema as link_schema


class Query(link_schema.Query, graphene.ObjectType):
    pass


class Mutation(link_schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
