import random

guessed = False

print("Guess the number from 0-20")
number = random.randint(0, 20)

while not guessed:
    user_try = int(input())
    if user_try > number:
        print("secret number is smaller")
    elif user_try < number:
        print("secret number is greater")
    else:
        print("congratulations! You are right")
        guessed = True

