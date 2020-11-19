from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from apps.endpoints.views import EndpointViewSet
from apps.endpoints.views import MLAlgorithmViewSet
from apps.endpoints.views import MLAlgorithmStatusViewSet
from apps.endpoints.views import MLRequestViewSet

router = DefaultRouter(trailing_slash = False)
router.register(r"enpoints", EndpointViewSet, basename = "endpoints")
router.register(r"mlalgorithm", MLAlgorithmViewSet, basename = "mlalgorithm")
router.register(r"mlalgorithmstatuses", MLAlgorithmStatusViewSet, basename = "mlalgorithmstatuses")
router.register(r"mlrequest", MLRequestViewSet, basename = "mlrequest")

urlpatterns = [
	url(r"^api/v1/", include(router.urls)),
]