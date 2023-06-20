from django.views import generic
from .models import Goods
from .forms import GoodsCreateForm, GoodsUpdateForm
from django.urls import reverse_lazy


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

