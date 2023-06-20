# pythonで if 変数:　と書いた時、空と認定されるもの一覧

a = []
# a = ''
# = 0
# a = {}
# a = ()
# a = None
# a = False

if a:    # aに要素がある場合の書き方
    print('aは空ではない')
else:
    print('aは空')