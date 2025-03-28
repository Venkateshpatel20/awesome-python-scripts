# x = 5
# print(f"out side variable x value is {x}")
# def hello():
#     y = 6
    
#     print(f"the global variable x inside the function is {x}")#accesible outside the function
#     print(f"the local variable y is {y}")#accessing local variable
#     print("Hello harry")
# print(f"The Global x is {x}")
# #print(f"the value of local var in finction z is {z}")#raises a NameError
# hello()
# print(f"the global x is {x}")

# """lets see local and global keywords in python"""
# x = 10 #Global variable
# print(f"Before changing the x value {x}")
# def my_function():
#     global x
#     x = 4
#     y = 11
#     print(y)#Local variable
# my_function()
# print(f"after changing x value inside the function{x}")
# # print(y)#this is raises a NameError

# global w = 4
# print(w)
# def func1():
#     global w
#     w = 56
#     print(w)
# print(w)