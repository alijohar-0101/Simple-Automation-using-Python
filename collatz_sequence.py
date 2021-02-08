def collatz(number):
    if number == 1:
        print("Collatz Complete!!")
    elif number % 2 == 0: #if the number is even
        print(int(number/2))
        collatz(number/2)
    else: #if the number is odd
        print(int(number * 3 + 1))
        collatz(number * 3 + 1)


try: 
    collatz(int(input('Choose a integer greater than 1: ')))
except ValueError:
    print('Non-integer entered, EXIT')