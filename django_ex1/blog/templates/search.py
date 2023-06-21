# ページ遷移を検索条件に合致させる

from django import template
register = template.Library()


@register.simple_tag
def url_replace(request, field, value):
    """GETパラメータを一部を置き換える"""

    # GETパラメータをコピーする（辞書の型）
    url_dict = request.GET.copy()

    # GETパラメータ辞書['page'] = 1
    url_dict[field] = str(value)

    # URLのGETパラメータ文字列を作成する
    return url_dict.urlencode()
