total = 0
with open('../sales.txt', 'r', encoding='utf-8') as sales:
    for row in sales:
        total += int(row)

surplus = 0
with open('../sales.txt', 'r', encoding='utf-8') as sales:
    for row in sales:
        if int(row) >= 0:
            surplus += int(row)

deficit = 0
with open('../sales.txt', 'r', encoding='utf-8') as sales:
    for row in sales:
        if int(row) < 0:
            deficit += int(row)

print(total, surplus, deficit)
