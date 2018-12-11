def fizzbuzz():
    print('FizzBuzz')

def fizz():
    print('Fizz')

def buzz():
    print('Buzz')

def print_fizzbuzz():
    for num in range(1, 31):
        if num % 15 is 0:
            fizzbuzz()
        elif num % 3 is 0:
            fizz()
        elif num % 5 is 0:
            buzz()
        else:
            print(num)

print_fizzbuzz()
