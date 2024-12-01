import graphene
from graphene_django import DjangoObjectType

from .models import Escala


class EscalaType(DjangoObjectType):
    class Meta:
        model = Escala


class Query(graphene.ObjectType):
    escalas = graphene.List(EscalaType)

    def resolve_escalas(self, info, **kwargs):
        return Escala.objects.all()