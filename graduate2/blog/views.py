from django.core.exceptions import PermissionDenied
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

    def get_queryset(self):
        return super().get_queryset().filter(owner__isnull=True)


class PremiumPostListView(ListView):
    model = Post

    def get_queryset(self):
        return super().get_queryset().filter(owner__is_community=True)


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:premium_list',)

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            return super().form_valid(form)

        form.instance.owner = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    login_url = '../../users/'
    redirect_field_name = 'redirect_to'
    form_class = PostForm

    def get_success_url(self):
        return reverse('blog:post_detail', args=[self.kwargs.get('pk')])

    def get_object(self, queryset=None):
        if self.object.owner != self.request.user:
            return PermissionDenied("You're not the owner of this post")


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    login_url = '../../users/'
    redirect_field_name = 'redirect_to'
    success_url = reverse_lazy('blog:premium_list')

    def get_object(self, queryset=None):
        if self.object.owner != self.request.user:
            return PermissionDenied("You're not the owner of this post")
