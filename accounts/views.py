from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class LoginView(TemplateView):
    template_name = 'index.html'

class LogoutView(TemplateView):
    template_name = 'index.html'

class RegisterView(TemplateView):
    template_name = 'index.html'

login = LoginView.as_view()
logout = LogoutView.as_view()
register = RegisterView.as_view()