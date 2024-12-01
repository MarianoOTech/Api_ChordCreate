import graphene
from graphene_django import DjangoObjectType

from .models import InstrumentoImagen


class InstrumentImgType(DjangoObjectType):
    class Meta:
        model = InstrumentoImagen


class Query(graphene.ObjectType):
    instrumentImgs = graphene.List(InstrumentImgType, instrumento=graphene.String(), nota=graphene.String())

    def resolve_instrumentImgs(self, info, instrumento=None, nota=None, **kwargs):
        # Filtrar las imágenes según los argumentos proporcionados
        queryset = InstrumentoImagen.objects.all()
        if instrumento:
            queryset = queryset.filter(instrumento=instrumento)
        if nota:
            queryset = queryset.filter(nota=nota)
        return queryset
