from django.urls import path

from .views import LoginView, all_products, home, profile

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('', home, name='home'),
    path('profile/', profile, name='my_profile'),
    path('products/', all_products, name='all_products'),
]
