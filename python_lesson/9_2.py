# 引数が複数ある場合

def weather_report(place, weather):
    print('Today`s weather in ' + place + ' is ' + weather)

weather_report('Tokyo', 'Rain')

# 素数判定（関数を用いる場合）
def is_prime(number):
    # 引数のnumberが素数ならTrueを返す
    for j in range(2, number):
        # print(f'  j={j}')
        if i % j == 0:
            return False

    # 割り切れなかったら（素数じゃなかったら）ここに到達する
    return True


for i in range(2, 101):
    if is_prime(i):
        print(i)