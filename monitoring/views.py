from rest_framework import viewsets
from .models import MonitoredSite, ParseResult
from .serializers import MonitoredSiteSerializer, ParseResultSerializer

class MonitoredSiteViewSet(viewsets.ModelViewSet):
    queryset = MonitoredSite.objects.all()
    serializer_class = MonitoredSiteSerializer

class ParseResultViewSet(viewsets.ModelViewSet):
    queryset = ParseResult.objects.all()
    serializer_class = ParseResultSerializer