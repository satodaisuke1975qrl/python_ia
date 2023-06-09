# 演習問題1.
# 下に書きかけのプログラムがあります。
#
# 辞書のkeyとvalueをそれぞれinput関数で受けとり、user_dict辞書をprint関数で表示すると、
# {入力したkey: 入力したvalue}
# と表示されるプログラムを作成しましょう。
# (data_dict辞書にkey:valueを追加するという処理を書く必要があります)
#
# data_dict = {}
#
# key = input('keyを入力してください > ')  # 辞書のkeyを入力してもらう
# value = input('valueを入力してください > ')  # 辞書のvalueを入力してもらう
#
#
# print(data_dict)
#
#
# 演習問題2.
# 上のプログラムの末尾に1行追加し、辞書の「辞書オブジェクト[キー名]」構文を使い、入力したvalueをprint関数で表示してみましょう。
#
# 演習問題3.
# 上のプログラムの末尾に1行追加し、辞書のgetメソッドを使い、入力したvalueをprint関数で表示してみましょう。

# 1
data_dict = {}

key = input('keyを入力してください > ')
value = input('valueを入力してください > ')

data_dict[key] = value
print(data_dict)

# 2
print(data_dict[key])

# 3
print(data_dict.get(key))

