from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.CharField(unique=True, max_length=40, verbose_name='user_email')
    is_premium = models.BooleanField(default=False, verbose_name='user_is_premium')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
