from django.urls import include, path
from rest_framework import routers

from .views import ProductViewSet

router = routers.DefaultRouter()
router.register("", ProductViewSet)
# router.register("images", ProductImageViewset)


urlpatterns = [
    path("", include(router.urls), name="products"),
]
