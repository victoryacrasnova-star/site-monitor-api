from rest_framework.routers import DefaultRouter
from .views import MonitoredSiteViewSet, ParseResultViewSet

router = DefaultRouter()
router.register('sites', MonitoredSiteViewSet)
router.register('results', ParseResultViewSet)
urlpatterns = router.urls