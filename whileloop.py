# i = int(input("enter a value:"))
# while i in range(10):
#     i = int(input("enter the number:"))
# print("your done")
count = 5
while count in range(70):
    if count == 45:
        continue
    print(count)
    count += 1
    if count == 49:
        break
print("You are out of the while loop")
