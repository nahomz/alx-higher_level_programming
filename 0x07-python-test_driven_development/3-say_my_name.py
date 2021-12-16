#!/usr/bin/python3
#Author Hileamlak M. Yitayew
"""Defines a function a that prints full name
"""


def say_my_name(first_name, last_name=""):
    """Prints a string in a formated manner
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
