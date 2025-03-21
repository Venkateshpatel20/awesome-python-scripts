l = ["one",2,"three"]
for i in l:
    print(i)
print(type(l))
print(l[0])
print(l[2])
print(l[1])
l.append(7)
s = [4,45,32,4]
s.sort()
print(s)
s.reverse()
print(s)
# p=s.sort(reverse=True)
print()
l2 = [4,65,2,6,43]
l2.sort()#here sorted() is a method which modifies a list permanently and returns None

print(l2)
l4 = [4,5,3,54,1,2]
print(sorted(l4))#here sorted() is a function that does't modifies existing list instead it creates one for temporary use
print(l4)
print(l4.sort())#Returns None
l2.sort(reverse = True)
print(l2)
l4.append(99)#adds 99 at last index
l5 = [2,3,4,5,88]
l5.reverse()#prints reverse of it
print(l5)
print(l4)
print(l4.count(1))
# print(l4.clear())#returns None
print(l4.index(99))
l4.insert(1,999)
print(l4)
m = l4.copy()
print(m)
m[1] = 454
print(m)
m.extend(l2)
print(m)
c = l2 + m +l4
print(c)
