from django.views import generic
from .models import Goods
from .forms import GoodsCreateForm, GoodsUpdateForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect


class GoodsCreate(generic.CreateView):
    form_class = GoodsCreateForm
    template_name = 'crud/goods_create.html'
    success_url = reverse_lazy('crud:goods_list')


"""
createで作成後にすぐ詳細画面にリダイレクトする場合は、
success_urlの代わりに以下のユーザー定義関数を挿入する

    def form_valid(self, form):
        goods = form.save()
        return redirect('crud:goods_detail', pk=goods.pk)
        
"""


class GoodsList(generic.ListView):
    model = Goods
    template_name = 'crud/goods_list.html'


class GoodsDetail(generic.DetailView):
    model = Goods
    template_name = 'crud/goods_detail.html'


class GoodsUpdate(generic.UpdateView):
    model = Goods
    form_class = GoodsUpdateForm
    template_name = 'crud/goods_update.html'

    def get_success_url(self):
        # リダイレクト先がデータのidを埋め込む場合（動的という）
        # このメソッドを上書きする
        goods = self.get_object()
        return reverse_lazy('crud:goods_detail', kwargs={'pk': goods.id})


class GoodsDelete(generic.DeleteView):
    model = Goods
    template_name = 'crud/goods_delete.html'
    success_url = reverse_lazy('crud:goods_list')

    # 削除処理の挙動を変更
    # DBから削除するのではなく、専用のフィールド(state_flag)をFalseにすることで、削除したことにする
    # 一覧画面からは消えるが、管理画面（admin）からは見えるようになっている
    # メソッドを上書き
    def form_valid(self, form):

        # リダイレクト先のURLを変更
        success_url = self.get_success_url()

        # モデルインスタンス.フィールド名 = 値 で、書き換えや代入ができます
        self.object.state_flag = False

        # saveメソッドで、DBのレコードの更新や作成ができる
        self.object.save()

        # self.object.delete()  # これが本来の削除処理
        return redirect(success_url)



