# 1から100までfor文で繰り返し、
# 3の倍数のときは「Fizz」
# 5の倍数のときは「Buzz」
# 15の倍数のときは「FizzBuzz」
# それ以外は数値を表示するプログラムを作りましょう。

num = range(1, 101)

for i in num:
    if i % 3 == 0 and i % 5 != 0:
        print('Fizz')
    elif i % 3 != 0 and i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    else:
        print(i)

