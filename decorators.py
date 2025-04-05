#python decorators are a powerful and versatile tool that allow you to
#modify the behavior of function and methods.They are a way to extend the functionality of a function or method without
#modifying its source code
"""A decorator is a function that takes another function as an argument and returns 
a function new function that modifies the behavior of the original functions .
The new function is often referred to an a 'decorator' function.The basic syntaxfor using 
is following way 
@decorator_function
def my_function():
    pass"""

def hello():
    print("Hello world!")
hello()