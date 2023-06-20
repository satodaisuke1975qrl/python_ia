# カプセル化
# 外部参照しなくても良いものにつける

class Character:

    def __init__(self, name, level, level2):
        self.name = name
        # levelには外からアクセスしないでほしい（カプセル化「._」）
        # アンダースコアが１つの場合は、アクセスしようと思えばできる
        self._level = level
        # アンダースコアが２つの場合は、アクセスが完全にできない
        # 外側でprintしようとしても、エラーになる
        self.__level2 = level2

        # メソッドも同様にカプセル化できる
        def _speak(self):
            print()


taro = Character('taro', 10, 20)

print(taro.name)
print(taro.__level2)

