from django.db import models

NULLABLE = {'null': True, 'blank': True}


class DefaultPost(models.Model):
    title = models.CharField(max_length=50, verbose_name='Post_title')
    description = models.TextField(verbose_name='Post_description')
    image = models.ImageField(upload_to='media/post/', **NULLABLE, verbose_name='Post_image')

    class Meta:
        verbose_name = 'Default'
        verbose_name_plural = 'Defaults'


class PremiumPost(models.Model):
    title = models.CharField(max_length=50, verbose_name='Post_title')
    description = models.TextField(verbose_name='Post_description')
    image = models.ImageField(upload_to='media/post/', **NULLABLE, verbose_name='Post_image')

    class Meta:
        verbose_name = 'Premium'
        verbose_name_plural = 'Premiums'
