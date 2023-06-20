from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('tag/list/', views.TagListView.as_view(), name='tag_list'),
    path('article/list/', views.ArticleListView.as_view(), name='article_list'),
    path('article/detail/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('tag/create/', views.TagCreateView.as_view(), name='tag_create'),
    path('article/create/', views.ArticleCreateView.as_view(), name='article_create'),
    path('article/update/<int:pk>/', views.ArticleUpdateView.as_view(), name='article_update'),
    path('article/delete/<int:pk>/', views.ArticleDeleteView.as_view(), name='article_delete')
]
