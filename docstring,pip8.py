"""python docstrings are literals that comes 
right after a definition of a function,
method,class or module"""
def addition(x,y):
    '''This function simply gives the sum of two numbers'''
    return x+y
print(addition(5,5.665))
print(addition.__doc__)#prints  This function simply gives the sum of two numbers
#we need to include a doc string just after below function name or above the function name 
def multiply(x,y):
        return x*y
        '''This function simply gives the product of two numbers'''
print(multiply.__doc__)#it returns None
"""     
PEP8 
it is a document that provides the 
guidelines and best practice on how to 
write python code  
"""
"""
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
