from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):

    # Userモデルに元々あるが、
    # ユニークにしたい（オリジナルのアドレスに書き換えたい）ので
    # emailフィールドを上書き
    email = models.EmailField('メールアドレス', unique=True)

    # Userモデルにないフィールドを追加
    age = models.PositiveIntegerField('年齢', blank=True, null=True)


"""
    # Django開発でよくあるパターン
    # カスタムユーザーモデルを使うが、passで定義しておく
    # 将来的な変更に備えて、カスタムユーザーモデルを定義するだけしておく
    # passとしているので、中身は普通のUserモデルと同じですが
    # 途中からデフォルトユーザー→カスタムユーザー に変更する操作がないので、
    # エラーなどが起きにくい

    pass

    # この方法であれば、AbstractBaseUserに変更して細かくカスタマイズしたり
    # AbstractUserを継承したままフィールドを追加したり
    # passのまま普通のUserのフィールドと同じ状態で使えたりする
    # 臨機応変な対応が可能
"""




