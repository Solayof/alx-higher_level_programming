#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number <= 0:
    digit = ((number * -1) % 10) * -1
else:
    digit = number % 10
msg = f"Last digit of {number:d} is {digit}"
if digit > 5:
    print(msg + " and is greater than 5")
elif digit == 0:
    print(msg + " and is 0")
elif digit < 6 != 0:
    print(msg + " and is less than 6 and not 0")
