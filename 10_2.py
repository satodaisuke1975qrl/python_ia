# コンストラクタ

class Character:

    # ダンダーイニット。特殊メソッドと呼ぶ
    def __init__(self, name):
        self.name = name

    # メソッドの第一引数は、ほぼ必ず、インスタンス自身が渡される
    def speak(self, comment):
        print(self.name + ':' + comment)


# インスタンスの属性は、基本的にはコンストラクタの__init__で行う
# 他のメソッド内から、インスタンスの属性を設定することもあります
# taro.name = 'jiro' のように外側から設定することは少ないです
taro = Character('taro')
taro.speak(comment='ハロー')

# self.nameと同じ。結果的に、'taro'が取得できる
print(taro.name)