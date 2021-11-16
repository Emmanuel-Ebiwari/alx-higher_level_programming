#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
string = "Last digit of"
if last_digit > 5:
    print("{} {: d} is {: d} and is
          greater than 5".format(string, number, last_digit))
elif last_digit == 0:
    print("{} {:d} is {:d} and is 0".format(string, number, last_digit))
elif last_digit < 6 and not 0:
    print("{} {: d} is {: d} and is less
          than 6 and not 0".format(string, number, last_digit))
