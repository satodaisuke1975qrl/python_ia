from django.db import models

# Create your models here.


class StaffInformation(models.Model):

    staff_name = models.CharField('名前', max_length=100)
    email = models.EmailField('メールアドレス', blank=True, null=True)
    address = models.CharField('住所', blank=True, null=True, max_length=100)
    birthday = models.DateTimeField('誕生日', blank=True, null=True)
    hire_date = models.DateField('入社日', blank=True, null=True)
    at_desk = models.BooleanField('出社状態', default=False)

    def __str__(self):
        return self.staff_name


class Department(models.Model):
    name = models.CharField('部署名', unique=True, max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField('書籍名', max_length=100)
    management_code = models.CharField('管理番号', unique=True, max_length=50)

    def __str__(self):
        return self.name


class Staff(models.Model):

    # モデルのフィールドが多すぎるときや、一部のフィールドに頻繁にアクセスする場合は
    # 頻繁にアクセスするフィールドを別のモデルとして定義し
    # 必要になった時だけ、OneToOneで紐づいたモデルの情報にアクセスする
    id = models.PositiveIntegerField('id', primary_key=True)

    name = models.CharField('ビジネスネーム', max_length=100)

    information = models.OneToOneField(
        StaffInformation, on_delete=models.CASCADE,
        verbose_name='社員情報', null=True, blank=True
    )

    department = models.ForeignKey(
        Department, on_delete=models.CASCADE,
        verbose_name="所属部署", null=True, blank=True
    )

    rented_books = models.ManyToManyField(
        Book,
        verbose_name="借りている本", null=True, blank=True
    )

    def __str__(self):
        return self.name
