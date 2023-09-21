from django.contrib import admin
from .models import User


@admin.register(User)
class PostAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'password')
    list_filter = ('phone_number',)
    search_fields = ('phone_number',)
