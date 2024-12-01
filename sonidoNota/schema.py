import graphene
from graphene_django import DjangoObjectType

from .models import SonidoNota


class SonidoNotaType(DjangoObjectType):
    class Meta:
        model = SonidoNota


class Query(graphene.ObjectType):
    SonidoNotas = graphene.List(
        SonidoNotaType,
        instrumento=graphene.String(),
        nota=graphene.String()
    )

    def resolve_SonidoNotas(self, info, instrumento=None, nota=None, **kwargs):
        queryset = SonidoNota.objects.all()
        if instrumento:
            queryset = queryset.filter(instrumento=instrumento)
        if nota:
            queryset = queryset.filter(nota=nota)
        return queryset
