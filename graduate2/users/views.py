import time

from django.contrib.auth.views import LoginView as BaseLogin
from django.contrib.auth.views import LogoutView as BaseLogout
from django.views.generic import CreateView

from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import User, UserPayment
from .forms import UserPhoneForm

import re
import stripe


class TitleMixin(object):
    title = None


class LoginView(TitleMixin, BaseLogin):
    template_name = 'users/login.html'
    title = 'Log in'


class LogoutView(TitleMixin, BaseLogout):
    pass


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
        user.is_active = True
        user.save()

        return redirect('users:payment')


@login_required(login_url='users:login')
def product_page(request):
    stripe.api_key = settings.STRIPE_API

    if request.method == 'POST':
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': settings.PRODUCT_PRICE,
                    'quantity': 1,
                },
            ],
            mode='payment',
            customer_creation='always',
            success_url=settings.SITE_NAME + '/users/payment_successful?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=settings.SITE_NAME + '/users/payment_cancelled',
        )

        return redirect(checkout_session.url, code=303)

    return render(request, 'users/payment/product_page.html')


def product_success(request):
    stripe.api_key = settings.STRIPE_API

    checkout_session_id = request.GET.get('session_id', None)
    session = stripe.checkout.Session.retrieve(checkout_session_id)
    customer = stripe.Customer.retrieve(session.customer)

    user_payment = UserPayment.objects.get(user=request.user.id)   # user_id
    user_payment.payment_id = checkout_session_id
    user_payment.save()

    user = request.user
    user.is_community = True
    user.save()

    return render(request, 'users/payment/success.html', {'customer': customer})


def product_cancelled(request):
    return render(request, 'users/payment/cancel.html')


@csrf_exempt
def webhook(request):
    stripe.api_key = settings.STRIPE_API

    time.sleep(10)
    payload = request.body
    signature_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, signature_header, settings.STRIPE_WEBHOOK
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    if event['type'] == 'checkout_session_completed':
        session = event['data', 'object']
        session_id = session.get('id', None)
        time.sleep(15)

        user_payment = UserPayment.objects.get(payment_id=session_id)
        line_items = stripe.checkout.Session.list_line_items(session_id, limit=1)
        user_payment.is_paid = True
        user_payment.save()

    return HttpResponse(status=200)
