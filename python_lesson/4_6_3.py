food_list = ['ra-men', 'susi', 'kare-']
food_list2 = ['ra-men', 'susi', 'kare-']

# 値が同じならTrue
print(food_list == food_list2)

# 同じオブジェクトを指しているときはTrue（同じではないのでfalseが出力される）
print(food_list is food_list2)