"""map,filter are built-in functions in python for reduce we need to write "from functools import reduce" that allows us to 
apply a function on/over a sequence of elements and creates a new sequence.
These functions also known as higher order functions as they takes functions as arguments 
syntax of it map(function,iterable)"""
# def map_func(x):
    # return  x*x*x
list1 = [2,3,4,5,6,7,8]
# list2 = []
# for i in list1:
#     list2.append(map_func(i))
# list2 = map(map_func,list1)
# print(list2)#retuen a map object like <map object at 0x0000025572F29C00>
#if we converts into a list like this 
# list2 = list(map(map_func,list1))
# print(list2)#it will returns list of cubes in list format
# list5 = tuple(map(map_func,list1))
# print(list5)#it will returns list of cubes in tuple format
# list4 = str(map(map_func,list1))
# print(list4)#it will returns map object like this <map object at 0x0000023059D09ED0>
# #lets give a lambda as a function
# list3 = str(map(lambda x:x*x*x,list1))
# print(list3)
"""filter()
filter function filters a sequence of objects based on given 
predicate (a function that returns a boolean value) and returns a new 
sequence containing only that meet the predicate.
The filter function has the following syntax
filter(predicate,iterable)"""
# print(list1)
# def filter_func(x):
#     return x > 3
# filter_list = filter(filter_func,list1)
# print(list(filter_list))
# filter_list2 = tuple(filter(lambda x:x+x+x,list1))
# print(type(filter_list))
# print(filter_list)

# REDUCE()
"""the reduce function is a higher order function that applies a function to 
 a sequence and returns a single value .
 It is a part of the function module in python and has the following syntax
 reduce(function,iterable)
 The function arguments takes two arguments and returns a single value.
 The the itereble argument is a sequence of elements,such as a list/tuple.
  The reduce function applies the function to first two elements in iterable and then applies to 
   the function to result and next element and so on, The reduce function returns the final result. """


from functools import reduce

# List of numbers
numbers = [1,2,3,4,5,6,7,8,9,10]

#calculate the sum of the numbers using the reduce functions
sum = reduce(lambda x,y:x + y,numbers)
print(sum)