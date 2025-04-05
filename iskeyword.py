# is and ==
# is keyword compares the exact location of memory ,where as == compares the values
# a = 4
# b = "4"
# c = 4
# d = "4"
# print(a is b)#compares the location in memory and it is False
# print(a == b)#values and it is False
# print(a is c)#True
# print(b is d)#True
# print(a == c)#True
# print(b == d)#True
# z = [1,3,22]
# y = [1,3,22]
# print(z is y)#False
# print(z == y)#True
#when we compares a constant ,string or tuple any immutable items "is" returns True
# a = "hello"
# b = "hello"
# print(a is b)#returns True
# print(a == b)#returns True
# f = ("hello")
# j = ("hello")
# print(f is j)#returns True
# print( f == j)#returns True
# d = {"key:8"}
# k = {"key:8"}
# print(k is d)#returns False
s = None
l = None
print(l is s)#returns True
print(l is None)#returns True
# m = True
# z = True
# print(m is z)#returns True