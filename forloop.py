a = "hello world"
for i in a:
    print(i)
    if (i==" "):
        print("this is space")
list1 = ["red","yellow","blue"]
for list in list1:
    print(list,end="\n")
    for i in list:
        print(i,end="\t")
        print("\n")
#range()
# for i in range(5):#same as range(0,5)
#     print(i)
# for i in range(0,5,1):
#     print(i)
for i in range(1,5):
    print(i)#prints 1,2,3,4
for i in range(1,50,2):
    print(i , end=",")
print("\n")
for i in range(0,50,2):
    print(i,end=",")