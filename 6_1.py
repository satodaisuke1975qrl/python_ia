# 辞書（keyとvalueを持つ）
# PHPの連想配列と一緒

japanese_to_english = {
    '水': 'water',
    '風': 'wind',
    '火': 'fire',
    1: 'one',
    (1, 1, 1): 6,
    (6, 6, 6): 3,
}

# 辞書のアクセス方法
print(japanese_to_english[(1, 1, 1)])
print(japanese_to_english['水'])

# 要素の取得（無い時はNoneが出力される）
print(japanese_to_english.get('風'))
print(japanese_to_english.get('山'))
