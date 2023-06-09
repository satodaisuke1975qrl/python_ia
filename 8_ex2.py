for dividend in range(2, 101):
    prime = True
    for divisor in range(2, dividend):
        if dividend % divisor == 0:
            prime = False
    if prime:
        print(dividend)
