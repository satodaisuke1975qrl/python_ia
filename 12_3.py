import csv

# utf-8-sigを使うと、WindowsのExcelでCSVを綺麗にできる
# 通常のテクストエディタでも文字化けせずにCSVを表示できる
# BOM付きutf-8と呼ぶこともある
with open('data.csv', 'w', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['taro', '15', '札幌', 'a@a.com'])
    writer.writerow(['jiro', '16', '東京', 'b@b.com'])
    writer.writerow(['saburo', '17', '沖縄', 'c@c.com'])

with open('data.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
        print(row[0])
