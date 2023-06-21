from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.urls import reverse_lazy
from .models import Article, Tag, Comment
from .forms import TagCreateForm, ArticleCreateForm, ArticleUpdateForm, SearchForm, CommentCreateForm
from django.db.models import Q
from django.shortcuts import redirect


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


class ArticleSearchView(generic.ListView):
    model = Article
    template_name = 'blog/article_search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = super().get_queryset().order_by('created_at')
        form = SearchForm(self.request.GET)
        form.is_valid()

        keyword = form.cleaned_data.get('keyword')

        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(text__icontains=keyword)
            )

        return queryset


class CommentCreateView(generic.CreateView):
    model = Comment
    template_name = 'blog/comment_create.html'
    success_url = reverse_lazy('blog:article_list')
    form_class = CommentCreateForm

    def form_valid(self, form):

        # form.save(commit=False) データベースにはまだ保存しない
        # commit=Falseビューで、モデルのフィールドを埋めるための引数
        comment = form.save(commit=False)

        # Commentモデルの、targetフィールドをここで埋める
        # モデル名.objects.get(フィールド=値) １値だけDBから取り出すときに使うのがget
        # url内の<int:pk>は、self.kwargs['pk']で取得できる
        comment.target = Article.objects.get(pk=self.kwargs['pk'])

        # saveしないと保存されない
        comment.save()

        return redirect('blog:article_list')

