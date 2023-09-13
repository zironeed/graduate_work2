from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from blog.forms import PostForm
from blog.models import Post


class MainView(ListView):
    model = Post
    template_name = "blog/main.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Main"
        return context


class DefaultPostListView(ListView):
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return super().get_queryset().filter(owner__isnull=True)


class PremiumPostListView(ListView):
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return super().get_queryset().filter(owner__isnull=False)


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:premium_list',)
