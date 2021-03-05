from django.shortcuts import render
from rest_framework import viewsets
from base.models import Manga
from api.serializers import MangaSerializer
from rest_framework.response import Response

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache


CACHE_TTL = 60 * 5



# @method_decorator(cache_page(CACHE_TTL), name='list')
class MangaViewSet(viewsets.ViewSet):
    """
   return {
            "id":{
                 "id": ,
                 "name_ru":  ,
                 "type": ,
                 "image": ,
                 }
            }
    """
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer

    def list(self, *args) -> dict():
        query_params = self.request.query_params
        ids = query_params['id'].split(',')
        queryset = Manga.objects.filter(id__in=ids)
        serializer = MangaSerializer(queryset, many=True)
        data = {}
        for object in serializer.data:
            data[object['id']] = object
        return Response(data)

