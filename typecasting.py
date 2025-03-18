a = "1"
b = "2"
c= 1
d= 2
#implicit type conversion
print(a+b)#12
print(c+d)#3
#explicit type conversion
print(str(c)+str(d))#12
print(int(a)+int(b))#3
#Lets do an excercise
string = "15"
number = 7
stringnumber = int(string)#throws an error if the string is not  a valid integer
sum= number + stringnumber
print("sum of both numbers:",sum)
#implicit type conversion
x = 12
y = 1.4
print(x+y)
