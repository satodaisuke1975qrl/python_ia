# ファイル書き込み

with open('../sample.txt', 'w', encoding='utf-8') as file:
    file.write('1行目\n')
    file.write('2行目\n')


# # with文を使わない場合、以下のような処理になる
# file = None
# try:
#     file = open('sample.txt', 'w', encoding='utf-8')
# except Exception:
#     # エラーがあった場合の処理を書き込む
#     pass
# finally:
#     if file:
#         file.close() # ファイルは必ずクローズする
