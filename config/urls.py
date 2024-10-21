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
    path("api/v1/", include("apps.products.urls")),
    path("api/v1/info/", include("apps.info.urls")),
    path('api/v1/', include('apps.customers.urls')),
    path('api/v1/', include('apps.warehouses.urls')),
    path('api/v1/', include('apps.sales.urls')),
    path('', include('apps.users.urls')),
]+drf_yasg_urlpatterns+token_urlpatterns

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
