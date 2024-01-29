from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import InfoModelViewSet

router = DefaultRouter()
router.register("", InfoModelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
