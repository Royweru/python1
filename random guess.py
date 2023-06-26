import os
import random

guess = random.randint(1, 10)

number = input('please enter a number between 1-10: ')
num = int(number)
if num == guess:
    print("you won!")
    print(f'the random no was {guess}')

else:
    print("you lost")
    print(f'the random number was {guess}')
