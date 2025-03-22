# #set is a well defined object
# #it does't allows redundent values
# #immutable datatype
# #elements are unordered
# l1 = {2,3,4,2,1,-1}
# l2 = {"hello", 13 , False, 8.5 , True}
# for value in l2:
#     print(value)
# print(l1)
# print(l2)
# #lets create empty set
# empty_Set1 = {None}
# empty_Set2 = set()
# print(type(empty_Set1))
# print(type(empty_Set2))
#Operations on sets
s1 = {None}#if i write s1 = set() it will print set()
s11 = {"how",999}
s2 = {"Hello", "how", 1, True, False, 3.88}
print(s1)
print(s2)
print(s11)
# s1 = s1.union(s2)
# print(s1)
# s2.update(s1)#updates s1 with s2 elements
# print(s2)
s3 = s11.intersection(s2)
print(s3)