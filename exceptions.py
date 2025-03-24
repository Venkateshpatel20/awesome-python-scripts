a = input("enter a number:")
print(f"MUltiplication table for {a} is")
try:

    for i in range(1,11):
        print(f"{a} X {i} = : {int(a)*i}")
except Exception as e:
    print("invalid input")
finally:
    print("after try block")
#handling a specific error
try:
    num : int(input("Enter a number:"))
except ValueError:
    print("Number entered is not an integer")
list = []
try :
    num = int(input("enter a index number:"))
    print(list[num])
except IndexError :
    print(f"there is no index {num}")


def func():
    list1 = ["h","e","e","l"]
    num = int(input("enter  value for index:"))
    print(list1[num])
    try:
        # index = int(num)
        print(list1[num])
        return 0
    except IndexError as e:
        print(e)
        print("uuu")
        return 1
    finally:
        print("hello")
c = func()
print(c)

# func()



