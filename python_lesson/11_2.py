# strメソッド
# デバッグをする際に用いられる
# 他の人が見やすいようなものを作る

class Character:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Character({self.name})ですよ'

taro = Character('たろう')

print(taro)