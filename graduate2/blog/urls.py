from django.urls import path

from graduate2.blog.apps import BlogConfig
from graduate2.blog.views import DefaultPostListView, PremiumPostListView, PostCreateView

app_name = BlogConfig.name


urlpatterns = [
    path('blog/posts/free', DefaultPostListView.as_view(), name='default_list'),
    path('blog/posts/premium', PremiumPostListView.as_view(), name='premium_list'),
    path('blog/posts/create', PostCreateView.as_view(), name='post_create'),
]
