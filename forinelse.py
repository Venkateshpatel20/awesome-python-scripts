#we can include a else in for loop or while loop as well
for i in range(0,10,2):
    print(i)
else :
    print('sorry no i')

n = 0
while n<=20:
    print(n)
    n+=2
else:
    print("else block")

while n <= 3:
    print(n)
    n += 1
    if n == 2:
        break
else :
    print("never executed")