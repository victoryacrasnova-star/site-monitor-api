from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import MonitoredSite, ParseResult
from .serializers import MonitoredSiteSerializer, ParseResultSerializer
from .services import check_site

class MonitoredSiteViewSet(viewsets.ModelViewSet):
    queryset = MonitoredSite.objects.all()
    serializer_class = MonitoredSiteSerializer

    @action(detail=True, methods=['post'])
    def check(self, request, pk=None):
        check_site(pk)
        return Response({"status": "site checked"})

class ParseResultViewSet(viewsets.ModelViewSet):
    queryset = ParseResult.objects.all()
    serializer_class = ParseResultSerializer

