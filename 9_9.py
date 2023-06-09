def plus_g(a):
    print('gの値は' + str(g) + 'です')
    b = a + g
    return b

g = 1
print(plus_g(3))
g = 3
print(plus_g(3))