# ファイル読み込み

with open('sample.txt', 'r', encoding='utf-8') as f:
    # text = f.read()
    # print(text)

    # 1行ずつ、ファイルの中身を取り出せる
    for line in f:
        # ファイルの各行には改行が必ずあるので、
        # print関数の際の改行を消しておく
        print(line, end='')