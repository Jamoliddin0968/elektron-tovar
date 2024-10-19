from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import LoginForm
from .models import Category, Product


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    # Поменяйте на нужный URL после успешного входа
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Здесь должна быть логика аутентификации пользователя
        return super().form_valid(form)


def home(request):
    # Получаем поисковый запрос из GET-запроса
    query = request.GET.get('q', '')
    categories = Category.objects.all()
    # Здесь можно добавить фильтрацию по популярным продуктам
    popular_products = Product.objects.all()

    if query:
        popular_products = popular_products.filter(
            title__icontains=query)  # Фильтрация продуктов по названию

    return render(request, 'home.html', {
        'categories': categories,
        'popular_products': popular_products,
        'query': query,  # Передаем запрос в шаблон для отображения в поисковом поле
    })


@login_required
def profile(request):
    return render(request, 'profile.html', {
        'user': request.user
    })


def all_products(request):
    category_filter = request.GET.get('category', None)
    if category_filter:
        products = Product.objects.filter(category__title=category_filter)
    else:
        products = Product.objects.all()

    categories = Category.objects.all()

    return render(request, 'all_products.html', {
        'products': products,
        'categories': categories,
        'selected_category': category_filter,
    })
