# Strings are immutable
a = "HEllo WORLd"
print(a)
print(len(a))
print(a.lower())
print(a.upper())
print(a)#is equals to initial a value
b = "!!!!Hello!!!!!"
print(b.rstrip("!"))#removes trailing exclamation marks
print(b.replace("Hello","World"))
c = "hello world !!!"
print(c.split(" "))#returns in a list format
print(c.capitalize())
str1 = "Welcome to the Console"
print(len(str1))

print(str1.center(50))
print(len(str1.center(50)))
#print(len(str1.center()))
print(b.count("!"))
print(b.endswith("!"))
print(str1.endswith("to",4,10))
#startswith
print(str1.startswith("Wel"))
# print("startswitch")

str3 = "He's name is Dan.He is an honest person"
print(str3.find("is"))#gives index of first occurence of "is"
print(str3.find("iss"))#prints -1 
str4 = "alphanumeric123"
str5 = "alphanumeric"
str6 = str(123)
print(str4.isalnum())#True
print(str5.isalnum())#True
print(str6.isalnum())#True
#isalpha() method
print(str6.isalpha())#False
#islower() method
print(str3.islower())#False
#islower()
print(str3.isupper())#False
#isprintable()
str7 = "it is a non printable string\n"
print(str7.isprintable())#False cause is \n
#isspace()
str8 = "        "
print(str8.isspace())#True
#istitle
str9 = "World Health Organisation" 
str10 = "world health Organisation" 
print(str9.istitle())#True
print(str10.istitle())#False
#swapcase
print(str9.swapcase())
#title
print(str9.title())
print(str9.casefold())
print(str9.count("Health"))
print(str9.encode())
print(str9.format)
# print(str9.format_map())






