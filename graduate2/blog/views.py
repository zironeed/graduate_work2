from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

# from graduate2.blog.forms import ProductForm, VersionForm
from graduate2.blog.models import PremiumPost, DefaultPost


class PostListView(ListView):
    pass
