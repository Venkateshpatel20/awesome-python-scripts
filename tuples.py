tup = (5,)#immutable, if we write tup = (5) it treates as a int and labels it class as a int,so add ,
# tup[0] = 33 returns a TypeError
print(type(tup),tup)
tup2 = ("string")
print(type(tup2))#prints <class 'str'>
tup3 = (True)
print(type(tup3))# prints bool
tup3 = (True,)
print(type(tup3))
print(len(tup3))#1
if True in tup3:
    print("    ii")
tup33 = tup3[0:1]
print(tup33)
# operations on tuples
tuple_a = ('India', 'Indonashia','US',"GERMANY")
list_a = list(tuple_a)
list_a[0] = "Pakistan"
list_a.append("Newziland")
list_a.pop(1)
print(list_a)
tuple_a = tuple(list_a)
print(tuple_a)
#let's see tuple concatenation
tup5 = tuple_a + tup3
print(tup5)
c = (3,3,4,4,56,77,3,8)
print(c.count(3))#2
print(c.index(3))#0
res = c.index(3,4,len(c))#here we are searching for three in index of1,4
print(res)