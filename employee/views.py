from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm


class HomeView(TemplateView):
    template_name = 'home.html'


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
