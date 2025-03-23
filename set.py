#set is a well defined object
#it does't allows redundent values
#immutable datatype
#elements are unordered
l1 = {2,3,4,2,1,-1}
l2 = {"hello", 13 , False, 8.5 , True}
for value in l2:
    print(value)
print(l1)
print(l2)
#lets create empty set
empty_Set1 = {None}
empty_Set2 = set()
print(type(empty_Set1))
print(type(empty_Set2))
#Operations on sets
s1 = {None}#if i write s1 = set() it will print set()
s11 = {"how",999}
s2 = {"Hello", "how", 1, True, False, 3.88}
print(s1)
print(s2)
print(s11)
s1 = s1.union(s2)
print(s1)
s2.update(s1)#updates s1 with s2 elements
print(s2)
s3 = s11.intersection(s2)
print(s3)
cities = {"HYD","DELHI","BOMBAY","DUBAI"}
cities1 = {"HYD","LOCKNOW","SURATH","PUNE"}
print("{}\n{}".format(cities,cities1))#we can also write as print(f"{cities}\n{cities1}")
cities_common = cities.intersection(cities1)
print(cities_common)
# cities.intersection_update(cities1)#this upadates the existing cities set permanently
# print(cities)
#symmetric elements
print(cities.symmetric_difference(cities1))#this prints elements not in common in two sets
#DIFFERENCE
print(cities.difference(cities1))#this prints the elements cities that are not in cities1
# print("  ")
# print(cities - cities1)

# print(cities and cities1)
# print(cities or cities1)

cities11 =  ( cities.symmetric_difference(cities1))
print(cities11)
#ISDISJOINT
#it returns TRUE if there is no common elements in common else false
print(cities.isdisjoint(cities1))#False
print(cities.issuperset(cities1))#FALSE

print(cities.issubset(cities1))#False
cities33 = set()
cities33.add("Helsinki")
print(cities33)
cities33.update({"Tokyo","Rio","Nirobi"})#wee can add more than one element at once
print(cities33)
#cities33.remove("Tokyo3")#which will raise an error as there is no Tokyo3
cities33.discard("Tokyo3")#which not  raise an error as Tokyo is not there
#pop() this pops last element but we don't know which one it is
print(cities.pop())
#del() deletes an set
exm  = {"tokyo","hyd"}
del exm
#print(exm) #raises NameError as shows exm is not defined
exm2 = {"hh","jj"}
exm2.clear()#makes the set empty
print(exm2)
#membership operator in
if "hh" in exm2:
    print("available")
else:
    print("not available")