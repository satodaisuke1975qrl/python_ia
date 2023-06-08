# user_file_text = """
# hoge
# fuga
# taro
# ziro
# saburo
# """
# この複数行のテキストを、splitメソッドでリストに分割し、アルファベット順に並び替えます。
# その後、joinメソッドを使う、
# fuga hoge saburo taro ziro
# と表示するプログラムを作成してください。

user_file_text = """
 hoge
 fuga
 taro
 ziro
 saburo
 """

user_file_list = user_file_text.split()
sorted_user_file_list = sorted(user_file_list)
print(sorted_user_file_list)
result = ' '.join(sorted_user_file_list)
print(result)