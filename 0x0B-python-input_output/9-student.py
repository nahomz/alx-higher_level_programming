#!/usr/bin/python3
"""Defiens a student class
that have to_json public method"""

class Student:
   """a class for a student
   """

   def __init__(self, first_name, last_name, age):
       """Initalizes a student object
       """

       self.first_name = first_name
       self.last_name = last_name
       self.age = age

   def to_json(self):
       """returns a json representatiion of
       the object
       """

       return self.__dict__


