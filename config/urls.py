"""
    config/urls.py
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .yasg_urls import drf_yasg_urlpatterns

token_urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/products/", include("apps.products.urls")),
    path("api/v1/info/", include("apps.info.urls")),
    path('api/v1/categories/', include('apps.categories.urls')),
    path('api/v1/warehouse/', include('apps.warehouses.urls')),
    path('api/v1/sales/', include('apps.sales.urls')),
]+drf_yasg_urlpatterns+token_urlpatterns

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
