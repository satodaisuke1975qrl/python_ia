# range関数(繰り返し処理が可能な数字の組を自動生成)

r1 = range(10)
# r = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] と同じ意味

for i in r1:
    print(i, end=' ')

print('\n')

r2 = range(1, 10)

for i2 in r2:
    print(i2, end=' ')

print('\n')

r3 = range(0, 10, 2)

for i3 in r3:
    print(i3, end=' ')