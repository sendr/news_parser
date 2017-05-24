from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import NewsSerializer
from apps.core.models import News


class NewsList(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = News.objects.filter(site=kwargs['site'])
        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data)
