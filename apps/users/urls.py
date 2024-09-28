from django.contrib.auth import views as auth_views
from django.urls import path

from apps.users.views import CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_view(template_name='login.html'), name='login'),
]
