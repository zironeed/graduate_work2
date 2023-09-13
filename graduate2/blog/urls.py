from django.urls import path

from blog.apps import BlogConfig
from blog.views import DefaultPostListView, PremiumPostListView, PostCreateView

app_name = BlogConfig.name


urlpatterns = [
    path('posts/free/', DefaultPostListView.as_view(), name='default_list'),
    path('posts/premium/', PremiumPostListView.as_view(), name='premium_list'),
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
]
