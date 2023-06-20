from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.urls import reverse_lazy
from .models import Article, Tag
from .forms import TagCreateForm, ArticleCreateForm, ArticleUpdateForm


class Home(generic.TemplateView):
    template_name = 'blog/home.html'


class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = 'blog/article_detail.html'


class ArticleListView(generic.ListView):
    model = Article
    template_name = 'blog/article_list.html'


class TagListView(generic.ListView):
    model = Tag
    template_name = 'blog/tag_list.html'


class TagCreateView(generic.CreateView):
    model = Tag
    template_name = 'blog/tag_create.html'
    success_url = reverse_lazy('blog:tag_list')  # テンプレートで使った、urlタグみたいなもの
    form_class = TagCreateForm


class ArticleCreateView(generic.CreateView):
    model = Article
    template_name = 'blog/article_create.html'
    success_url = reverse_lazy('blog:article_list')
    form_class = ArticleCreateForm


class ArticleUpdateView(generic.CreateView):
    model = Article
    template_name = 'blog/article_update.html'
    success_url = reverse_lazy('blog:article_list')
    form_class = ArticleUpdateForm


class ArticleDeleteView(generic.DeleteView):
    model = Article
    template_name = "blog/article_delete.html"
    success_url = reverse_lazy('blog:article_list')