from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Article, Tag


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
