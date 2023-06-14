from django.urls import path

# .は、今いる場所
from . import views

# 'myapp'の場所にはアプリ名が入る
app_name = 'myapp'

urlpatterns = [
    # どのURLでどのビュー（処理）を呼ぶかを登録する
    # path関数の第一引数にURLを入力する
    # 第二引数は、どのビューを呼ぶか
    path('hello/', views.hello, name='hello'),
    path('home/', views.home, name='home'),
    path('home2/', views.home2, name='home2'),

    # クラス
    # views.クラス名.as_view() と書く必要がある
    path('home3/', views.Home.as_view(), name='home3')
]