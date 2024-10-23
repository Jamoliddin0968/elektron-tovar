# urls.py
from django.urls import path

from .views import UserDetailView, UserListView

urlpatterns = [
    path('users/me', UserDetailView.as_view(), name='user_detail'),
    path('api/users/', UserListView.as_view(), name='user_list'),
]
