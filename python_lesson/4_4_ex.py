# 演習問題2
# 組み込みinput()を使って、「2023」と入力してエンターを押すと、
# 「今は2023年です。来年は2024年です」と表示されるプログラムを作りましょう。

# 組み込み関数inputは文字列型なので、数値型にしたい場合はintにする

num = input()
year = int(num)
print('今は'+ str(year) + '年です。来年は' + str(year+1) + '年です。')

