dic = {'商品A': 3, '商品B': 10, '商品C': 7, '商品D': 5}

print('商品一覧')

# 辞書のkeyの一覧を出す
for key in dic.keys():
    print(key)

print('\n商品と在庫数の一覧')
for key, value in dic.items():
    print('商品名：' + key + '\t在庫数：' + str(value))

# dic.items() は、以下のようなリストを作っている
tuple_list = [
    ('商品A', 3),
    ('商品B', 10),
    ('商品C', 7),
    ('商品D', 5)
]

for key, value in tuple_list:
    print(key)
    print(value)


# Pythonは、以下のような書き方が可能

key, value = ('商品名', 200)
