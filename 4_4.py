# 数値型から文字列型へ str()

s = 'My age is ' + str(18)
print(s)

# 文字列型から数値型へ int(), float()

a = '100'
b = '200'
sum_str = a + b
sum_int = int(a) + int(b)
print(sum_str, sum_int)

# 組み込み関数inputは文字列型なので、数値型にしたい場合はintにする
