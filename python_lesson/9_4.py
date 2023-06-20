# sは仮引数とも呼ぶ
def message(s=None):
    if s is None:
        print('文字列未入力')
    else:
        print('入力文字列 > ' + s)

# 'Hello, World'は実引数とも呼ぶ
message('Hello, World')
# 関数を呼び出すときに、仮引数=値の形にすることもできる
message(s = 'Hello, World')
message()
