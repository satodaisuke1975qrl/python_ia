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
    path('home/', views.home, name='home')
]