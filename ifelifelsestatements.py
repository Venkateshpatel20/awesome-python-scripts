#conditional statemnts in python 
"""
if
elif
else
nested if

"""
a =int(input("enter your age:"))
print("your age is:",a)
if a>18:
    pass
    print("Yeah")
elif (a<=18):
    pass
    print("No")
else :
    print("Invalid input")

#Let's use elif statement
b = int(input("enter a number:"))
print("you entered number:",b)
if ( b<0):
    print("You Entered a negative number")
elif( b == 0):
    print("You entered zero")
else :
    print("You entered a positive number")

# else:
#     print("Please enter a valid number")
    
#nested if statements
b = float(input("Enter a number:"))
if(b<0):
    print('You entered a negative number')
elif(b>0):
    if(b<=10):
        print("You entered a number between one and ten")
    elif(b>10 and b<100):
        print("You entered a value between 10 and 100")
    else:
        print("You entered  value greater than a 100")
else:
    print("You entered zero")

###datetime module
import time
print(time.now())
