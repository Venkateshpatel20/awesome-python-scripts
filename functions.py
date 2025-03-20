#we use def keyword to define a function
def addTwoNumbers(a,b):
    sum = (a+b)
    return sum
print(addTwoNumbers(2,4))#this is required type of giving parameters
def suB(d=4,c=7):#way of giving a default parameters
    return (d-c)
print(suB(d=11,c=17))#providing two inputs
print(suB(d=17))#passing first variable value
print(suB(c=17))#passing values for second variable
def maxNum(a,b):#default arguments will be given here if you wish
    if a>b:
        print(str(a)+" is grater number than b")
    elif b>a:
        print(str(b) +" is greater than a")
    else :
        print("Two numbers are equal")
a = float(input("enter a number:"))
b = float(input("enter a number:"))
maxNum(a,b)#required arguments will be passed from here if you dont given a default ones
# maxNum()
def avg(*numbers):
    sum = 0 
    print(type(numbers))#tuple
    for number in numbers:
        sum = number + sum
    return (sum/len(numbers))
print(avg(2,4,3))
c = avg(4,5)
print(c)
def hello(**names):
    print(type(names))#dictionary
    for name in names:
        print("hello," ,name)