pref = '愛知県 , 富山県 , 三重県'
a = pref.split(',')
print(a)

pref2 = '東京都 神奈川県 埼玉県 千葉県'
b = pref2.split()
print(b)

text = 'apple,banana,orange'
food_list = text.split(',')
print(food_list)

food_list = ''.join(food_list)
print(food_list)
food_list = ','.join(food_list)
print(food_list)
