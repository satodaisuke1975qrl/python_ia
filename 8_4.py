# continue

number_list = [12, 34, 5, 6, 32, 67, -3, 14, 35]

for i in number_list:
    if i < 10:
        continue

    print(i)  # 10より小さい数が出てきたら飛ばす
