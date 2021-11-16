#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last = number % -10
else:
    last = number % 10
if last > 5:
    print("Last digit of {0:d} is {1:d}".format(number, last), end=' ')
    print("and is greater than 5")
elif last == 0:
    print("Last digit of {0:d} is {1:d} and is 0".format(number, last))
elif last < 6 and last != 0:
    print("Last digit of {0:d} is {1:d}".format(number, last), end=' ')
    print("and is less than 6 and not 0")
