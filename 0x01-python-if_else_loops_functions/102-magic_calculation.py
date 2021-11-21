#!/bin/python3


def magic_calculation(a, b, c):
    """"Returns c if a < b
    returns a +b if !(a < b) and c >b
    if none of the case are satisfied it
    returns a*b-c """

    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return a * b - c
