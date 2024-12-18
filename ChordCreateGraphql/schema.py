import graphene
import graphql_jwt

import escalas.schema
import instrumentoImg.schema
import sonidoNota.schema

#user
import users.schema

class Query(
    users.schema.Query,
    escalas.schema.Query, 
    instrumentoImg.schema.Query,
    sonidoNota.schema.Query,
    graphene.ObjectType
):
    pass

class Mutation(users.schema.Mutation, graphene.ObjectType,):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)