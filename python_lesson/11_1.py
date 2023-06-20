# 継承とオーバーライド
# 親クラスの内容を子クラスが引き継ぐ


class Character:

    def __init__(self, name):
        self.name = name

    def speak(self, comment):
        print(self.name + ':' + comment)


# ()の中に親クラスの名前を入れる
class Healer(Character):
    # pass
    # passは定義するものがないときに使う

    # initも上書きができる
    # スーパークラス
    # super().親クラスのメソッド名 という書き方をする
    def __init__(self, name, power):
        super().__init__(name)
        self.power = power

    # オーバーライド
    def speak(self, comment):
        super().speak(comment)
        # 喋ったあとに、回復もするように上書きした
        self.healing()

    def healing(self):
        print(f'{self.name}はパワーを{self.power}回復した')

taro = Healer('たろう', 80)

taro.healing()

taro.speak(comment='ハロー')
