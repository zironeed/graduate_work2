from django.urls import path

from .apps import UsersConfig
from .views import RegisterView, LoginView, LogoutView, product_page, \
    product_cancelled, product_success, webhook

app_name = UsersConfig.name


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('user/registration/', RegisterView.as_view(), name='user_register'),

    path('user/payment/', product_page, name='payment'),
    path('payment_successful', product_success, name='payment_successful'),
    path('payment_cancelled', product_cancelled, name='payment_cancelled'),
    path('stripe_webhook', webhook, name='webhook'),
]
