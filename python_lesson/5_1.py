data_list = [2, 5.6, 'abcde',{}]

print(data_list[2:])

# 空リストの作成
data_list = []

# リストの中にリストを入れる（インテンド揃えなきゃダメ）
data_list2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(data_list2)

# [1,2,3]を取り出す
print(data_list2[0])

# 5を取り出す
print(data_list2[1][1])

# データの書き換え（リストは書き換えられるが、文字列は書き換えられない）
data_list2[1] = [10,20,30]
print(data_list2)

# 要素の追加
food_list = ['apple', 'orange', 'lemon']
print(food_list)
# 末尾追加
food_list.append('grape')
print(food_list)
# 位置を指定して追加（[2]の位置に追加する場合）
food_list.insert(2, 'banana')
print(food_list)

# 要素の削除
del food_list[0]
print(food_list)

# 空文字列（白紙のノート的なもの）
text = ""
