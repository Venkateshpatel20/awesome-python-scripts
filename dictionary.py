#Dictionaries in python are ordered collection of data items.They store multiple items in a single variable.
#Dictionary items are key value-pairs they are seperated by commas and enclosed inside curly braces {}
info = {"name":'patel'
        , "age":19,"sex":"M","eligible":True,55:"Ram",}
print(type(info))#<class 'dict'>
print(info)
#accesing single_value using key using []
print(info["name"])#patel
print(info[55])#Ram
print(info.get("eligible"))#another way to get info
#different outputs for above methods if i try to access a value for a key that not in dictionary
# print(info.get("eligible1"))#prints None
# print(info[555])#raises a KeyError
""" how can we access all keys or values"""
print(info.keys())# gives all keys
print(info.values())# gives all values
for key in info.keys():
    print(f"the value corresponding to {key} is {info[key]}")
    
print(info.items())
for key , value in info.items():
    print(f"The corresponding value for key {key} is {value}")

info = {"name":'patel', "age":19,"sex":"M","eligible":True,55:"Ram"}
print(info.keys())
print(info.values())
print(info["name"])
print(info.get("eligible"))
for key in info.keys():
    print(f"{key} is {info[key]}")
print(info.items())
for key , value in info.items():
    print(f"value for {key} is {value}")

"""Lets explore some dictionary methods"""
"""update"""
ep1 = {122:45,123:34,132:54,666:67}
ep2 = {444:54,564:54}
ep1.update(ep2)
print(ep1)#{122: 45, 123: 34, 132: 54, 666: 67, 444: 54, 564: 54}
print(ep2)#{122:45,123:34,132:54,666:67}
"""clear()"""
# ep1.clear()
print(ep1)
empty_dictionary = {}
"""pop()"""
ep1.pop(444)
ep1.pop(564)
print(ep1)
"""popitem() //simply pops the last key valure pair"""
ep1.popitem()#removes 666:67
print(ep1)
"""del //it deletes the dictionary"""
# del ep1
# print(ep1)
del ep1[132]#deletes key 132
print(ep1)