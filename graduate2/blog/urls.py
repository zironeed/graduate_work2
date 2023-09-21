from django.urls import path

from blog.apps import BlogConfig
from blog.views import DefaultPostListView, PremiumPostListView, PostCreateView, PostDetailView, PostUpdateView, \
    PostDeleteView

app_name = BlogConfig.name


urlpatterns = [
    path('posts/society/', DefaultPostListView.as_view(), name='default_list'),
    path('posts/community/', PremiumPostListView.as_view(), name='premium_list'),
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('posts/detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
]
