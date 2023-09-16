from django.contrib.auth.views import LoginView as BaseLogin
from django.contrib.auth.views import LogoutView as BaseLogout
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, \
    PasswordResetCompleteView, PasswordResetDoneView

from django.views.generic import CreateView, TemplateView

from django.urls import reverse_lazy

from .models import User


class TitleMixin(object):
    title = None


class LoginView(TitleMixin, BaseLogin):
    template_name = 'users/login.html'
    title = 'Log in'


class LogoutView(TitleMixin, BaseLogout):
    template_name = 'users/logout.html'
    title = 'Log out'
