def get_tax(price):
    tax = int(price * 0.1)
    price_including_tax = int(price * 1.1)
    return (tax, price_including_tax)

# 複数の戻り値がある時、代入も複数の変数を指定できる
a,b = get_tax(100)
print(a, b)