#!/usr/bin/python3
#Author Hileamlak M. Yitayew
"""Defines the print_square function
"""


def print_square(size):
    """Prints a square
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        for y in range(size):
            print("#", end='')
        print()
