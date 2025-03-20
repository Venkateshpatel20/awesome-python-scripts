# i = int(input("enter a value:"))
# while i in range(10):
#     i = int(input("enter the number:"))
# print("your done")
count = 5
for count in range(70):
    
    print(count)
    count += 1
    if count == 45:
        print("elven")
        continue
 
    if count == 49:
        break
print("You are out of the while loop")
