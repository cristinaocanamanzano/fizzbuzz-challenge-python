def print_fizzbuzz():
    for num in range(1, 101):
        if num % 15 is 0:
            print('FizzBuzz')
        elif num % 3 is 0:
            print('Fizz')
        else:
            print(num)
