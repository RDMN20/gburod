from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    template_name = 'users/signup.html'
    redirect_field_name = 'next'

    def get_success_url(self):
        next_url = self.request.POST.get(self.redirect_field_name)
        if next_url:
            return next_url
        else:
            return reverse_lazy('main-page:index')

    def form_valid(self, form):
        to_return = super().form_valid(form)
        login(self.request, self.object)
        return to_return


class Login(LoginView):
    template_name = 'users/login.html'
    redirect_field_name = 'next'


