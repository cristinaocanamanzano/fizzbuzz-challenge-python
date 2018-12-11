def print_fizzbuzz():
    for num in range(1, 31):
        if num % 15 is 0:
            print('FizzBuzz')
        elif num % 3 is 0:
            print('Fizz')
        elif num % 5 is 0:
            print('Buzz')
        else:
            print(num)
