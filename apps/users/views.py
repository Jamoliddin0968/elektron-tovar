from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
