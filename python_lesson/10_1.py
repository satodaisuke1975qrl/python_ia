# クラス 単語の最初の文字は大文字にする
class CharacterData:
    name = 'taro'

    # メソッド クラスの中にある関数
    def speak(self, comment):
        print(self.name + ':' + comment)


# インスタンス化（クラスを使えるようにする。Characterのインスタンスを、taro変数に代入）
taro = CharacterData()

# インスタンスの中のspeak関数に代入
# selfとtaroは同じもの
taro.speak(comment = 'ハロー')

# クラスの外側でインスタンスの中身を変更できる
taro.name = 'jiro'
taro.speak(comment = 'ハロー')


# クラスのデータ属性に存在しなくても、自由に属性を追加できる
taro.first_name = "太郎"
taro.last_name = "田中"
print(taro.first_name)
print(taro.last_name)