from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import MonitoredSite, ParseResult
from .serializers import MonitoredSiteSerializer, ParseResultSerializer
from .services import check_site

class MonitoredSiteViewSet(viewsets.ModelViewSet):
    queryset = MonitoredSite.objects.all()
    serializer_class = MonitoredSiteSerializer

    def get_queryset(self):
        is_active = self.request.query_params.get('is_active')

        if is_active is not None:
            return MonitoredSite.objects.filter(is_active=is_active.lower() == 'true')
        return MonitoredSite.objects.all()

    @action(detail=True, methods=['post'])
    def check(self, request, pk=None):
        check_site(pk)
        return Response({
            "status": "site checked",
            "site_id": pk
        })

class ParseResultViewSet(viewsets.ModelViewSet):
    queryset = ParseResult.objects.all().order_by('-checked_at')
    serializer_class = ParseResultSerializer

