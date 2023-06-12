with open('sales.txt', 'r', encoding='utf-8') as sales:

    total = 0
    surplus = 0
    deficit = 0

    for i in sales:
        total = total + int(i)
        if int(i) > 0:
            surplus = surplus + int(i)
        elif int(i) < 0:
            deficit = deficit + int(i)


print(total, surplus, deficit)
