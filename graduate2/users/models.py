from django.contrib.auth.models import AbstractUser
from django.db import models

from blog.models import NULLABLE
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    username = None

    phone_number = models.CharField(unique=True, max_length=10, verbose_name='User_phone (without +7)', **NULLABLE)
    payment = models.OneToOneField('UserPayment', on_delete=models.CASCADE,
                                   verbose_name='User_payment', related_name='user_payment', **NULLABLE)
    is_community = models.BooleanField(default=False, verbose_name='User_is_community')

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class UserPayment(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, verbose_name='Payment_user')
    payment_id = models.CharField(max_length=100, verbose_name='Payment_id')
    is_paid = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'


@receiver(post_save, sender=User)
def create_user_payment(sender, instance, created, **kwargs):
    if created:
        UserPayment.objects.create(user=instance)
