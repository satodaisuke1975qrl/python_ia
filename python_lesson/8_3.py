# break

number_list = [12, 34, 5, 6, 32, 67, -3, 14, 35]

for i in number_list:
    if i < 0:
        print('処理停止')
        break
    else:
        print(i)