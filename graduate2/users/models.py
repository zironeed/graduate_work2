from django.contrib.auth.models import AbstractUser
from django.db import models

from blog.models import NULLABLE


class User(AbstractUser):
    username = None

    phone_number = models.CharField(unique=True, max_length=10, verbose_name='User_phone (without +7)', **NULLABLE)
    payment = models.OneToOneField('UserPayment', on_delete=models.CASCADE,
                                   verbose_name='User_payment', related_name='user_payment', **NULLABLE)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class UserPayment(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, verbose_name='Payment_user')
    payment_id = models.CharField(max_length=100, verbose_name='Payment_id')
    paid = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
