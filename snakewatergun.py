"""in this game a player try to make a gun or snake or water using their hand
Gun kills the Snake
Snake drinks Water
Water damages the Gun"""
# def game(x):
choice_list = ["Snake","Gun","Water"]
print("choose the your pic")
print("Snake")
print("Water")
print("Gun")
def user1():
    x = str(input("Enter player one choice:"))
    x = x.capitalize()
    x1 = None
    if x == "Snake":
        x1 = 1
        return x1
    elif x == "Water":
        x1 = 0
        return x1

    elif x == "Gun":
        x1 = -1
        return x1
    else:
        print("Choose Gun or Snake or Water")
def user2():
    x = str(input("Enter player  choice:"))
    x = x.capitalize()
    x1 = None
    if x == "Snake":
        x1 = 1
        return x1
    elif x == "Water":
        x1 = 0
        return x1

    elif x == "Gun":
        x1 = -1
        return x1
    else:
        print("Choose Gun or Snake or Water")
