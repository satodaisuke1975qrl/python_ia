# リストのソート

number_list = [15, 93, 34, 28, 38, 53, 2, 24]

# 昇順にソート
sorted_number_list = sorted(number_list)
print(sorted_number_list)

# 降順にソート
sorted_number_list = sorted(number_list, reverse=True)
print(sorted_number_list)

# sortメソッドでもいけるよ
number_list.sort()
print(number_list)

number_list.sort(reverse=True)
print(number_list)
