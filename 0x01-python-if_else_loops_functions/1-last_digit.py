#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 5:
    print(f"last digit of {number} is {number} and is greater than 5")
if number == 0:
    print(f"last digit of {number} is {number} and is 0")
elif number < 6:
    print(f"last digit of {number} is {number} and is less than 6 and 0")
