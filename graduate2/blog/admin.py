from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'owner',)
    list_filter = ('owner',)
    search_fields = ('title', 'owner',)
