from django.core.cache import cache

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from . import serializers
from . import models


class UrlCrud(ModelViewSet):
    serializer_class = serializers.UrlObjectSerializer
    lookup_field = 'shorten_url'

    def get_queryset(self):
        return models.UrlObject.objects.all()

    def retrieve(self, request, *args, **kwargs):
        UrlCacheObj = cache.get(f"{self.kwargs['shorten_url']}")
        
        if not UrlCacheObj:
            obj = self.get_object()
            cache.set(f'{obj.shorten_url}', obj)
            return super().retrieve(request, *args, **kwargs)

        serializer = self.get_serializer(UrlCacheObj)
        return Response(serializer.data)

url_create = UrlCrud.as_view({
    'post':'create',
})

url_update_delete_retrieve = UrlCrud.as_view({
    'get':'retrieve',
    'patch':'partial_update',
    'delete':'destroy',
})