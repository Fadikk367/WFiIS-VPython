import math

def check_if_primary(num):
    if num < 2:
        return False
    isPrimary = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            isPrimary = False
            break
    return isPrimary

def check_number(number):
    if number % 2 == 0:
        print('even')
    if check_if_primary(number):
        print('primary')
    if number % 2 == 1:
        print('odd')

num = int(input('Please enter a number to check: '))
print()
print('Given number is: ')
check_number(num)

