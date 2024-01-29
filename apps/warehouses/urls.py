from django.urls import include, path
from rest_framework import routers

from .views import WareHouseViewSet

router = routers.DefaultRouter()


router.register('', WareHouseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
