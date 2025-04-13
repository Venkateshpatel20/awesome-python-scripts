"""Getters
getters in python are methods that are used to access the values of an object's
properties . They ate used to return the values of a specific property and are typically 
defined using the @property decorator
, Here is an example of it"""
class myclass:
    def __init__(self, value):
        self._value = value
    @property