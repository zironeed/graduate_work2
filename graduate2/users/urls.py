from django.urls import path

from .apps import UsersConfig
from .views import RegisterView, LoginView, LogoutView, PaymentView

app_name = UsersConfig.name


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('user/registration/', RegisterView.as_view(), name='user_register'),
    path('user/payment', PaymentView.as_view(), name='user_payment')
]