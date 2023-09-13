from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from graduate2.blog.forms import PostForm
from graduate2.blog.models import Post


class DefaultPostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'default_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(owner__isnull=True)


class PremiumPostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'premium_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(owner__isnull=False)


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:premium_list',)
