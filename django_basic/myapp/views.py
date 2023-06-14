from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

def hello(request):
    return HttpResponse('<h1>Hello<h1>')

def home(request):
    return render(request, 'myapp/home.html')

class Character:

    def __init__(self, name):
        self.name = name

    def greed(self):
        print(f'{self.name}さん、こんにちは！')

def home2(request):
    context = {
        'title': 'ホーム2です',
        1: 2,
        'prime_list': [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31],
        'user': Character(name='taro')
    }
    return render(request, 'myapp/home2.html', context)


# home2をクラスで書き換えると以下のようになる
# TemplateView は、HTMLを単純に表示したいときに使う
class Home(generic.TemplateView):
    template_name = 'myapp/home2.html'

    # テンプレートファイルに追加で渡したいデータがある場合はこのメソッドを呼ぶ
    def get_context_data(self, **kwargs):

        # このメソッドに上書きする場合は、必ずsuper()で親のメソッドを継承する必要がある
        context = super().get_context_data(**kwargs)

        # 辞書[キーの名前]で、追加のデータを渡すことができる
        context['title'] = 'ホーム3です'
        context['prime_list'] = [1, 2, 3, 4, 5]
        return context

