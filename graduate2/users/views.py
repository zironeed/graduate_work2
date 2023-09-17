from django.contrib.auth.views import LoginView as BaseLogin
from django.contrib.auth.views import LogoutView as BaseLogout
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, \
    PasswordResetCompleteView, PasswordResetDoneView
from django.views import View
from django.views.generic import CreateView, TemplateView

from django.urls import reverse_lazy
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, reverse

from .models import User
from .forms import UserPhoneForm

import re


class TitleMixin(object):
    title = None


class LoginView(TitleMixin, BaseLogin):
    template_name = 'users/login.html'
    title = 'Log in'


class LogoutView(TitleMixin, BaseLogout):
    template_name = 'users/logout.html'
    title = 'Log out'


class RegisterView(TitleMixin, CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = UserPhoneForm
    title = 'Registration'
    success_url = reverse_lazy('blog:premium_list')

    def form_invalid(self, form):
        messages.error(self.request, "Invalid phone number.")
        return super().form_invalid(form)

    def form_valid(self, form):
        phone_number = form.cleaned_data['phone_number']

        if re.search('[a-zA-Z!@#$%^&*(),.?":{}|<>]', phone_number):
            form.add_error('phone_number', "Phone number should not contain letters or punctuation marks.")
            return self.form_invalid(form)

        user = form.save(commit=False)
        user.is_active = False
        user.save()

        return redirect('users:email_confirmation_sent')


class PaymentView(View):
    pass
