def fizzbuzz(minimum=1, maximum=100):

    for i in range(minimum, maximum+1):
        if i % 3 == 0 and i % 5 != 0:
            print('Fizz')
        elif i % 3 != 0 and i % 5 == 0:
            print('Buzz')
        elif i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        else:
            print(i)


fizzbuzz()

fizzbuzz(10, 20)



