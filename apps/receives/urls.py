from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ReceiveViewSet

router = DefaultRouter()
router.register("receive", ReceiveViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
