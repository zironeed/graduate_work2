from django.db import models

from django.conf import settings

NULLABLE = {'null': True, 'blank': True}


class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name='Post_title')
    description = models.TextField(verbose_name='Post_description')
    image = models.ImageField(upload_to='media/post/', **NULLABLE, verbose_name='Post_image')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='Post_owner')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
