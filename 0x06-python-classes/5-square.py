#!/usr/bin/python3
# 5-square.py

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, __size):
        """Initialize a new square.

        Args:
            __size (int): The __size of the new square.
        """
        self.__size = __size

    @property
    def size(self):
        """Get/set the current __size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("__size must be an integer")
        elif value < 0:
            raise ValueError("__size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
