"""Site-wide views for the Azure Tavern."""

from django.core import urlresolvers
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import FormView, RedirectView, TemplateView

class HomeView(TemplateView):
    template_name = 'index.html'

class RegisterView(FormView):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    success_url = urlresolvers.reverse_lazy('registration_complete')

class RegistrationCompleteView(TemplateView):
    template_name = 'accounts/complete.html'
