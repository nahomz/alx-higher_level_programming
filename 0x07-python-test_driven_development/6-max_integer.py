#!/usr/bin/python3


def max_integer(list=[]):
    if len(list) == 0:
        return None
    result = list[0]
    for x in list:
        if x > result:
            result = x
    return result
