a = 33;
b = 56;
print("A") if a > b else print('=') if a == b  else print("B")
c = 7 if a>b else 0
print(c)
def shorthand_ifelse_example(condition):
    """Demonstrate the shorthand if_else (ternary operator) in python"""
    result = "Condition is True" if condition else "condition is False"
    print(f"result using shorthand-ifelse is {result}")
    
    print(f"Result using shorthand ifelse:{result}")
def regularifelse_example(condition):
    """Demonastrates the regular if_else statement for comparision"""
    if condition:
        result="Condidtion is True"
    else:
        result = "Condition is False"
    print(f"Result using regular if_else:{result}")
if __name__ == "__main__":
    print("Example with condition True:")
    shorthand_ifelse_example(True)
    regularifelse_example(True)
    print("/nExample with condition False:")
    shorthand_ifelse_example(False)
    regularifelse_example(False)
    print("\nMore complex example:")
    value = 15
    message = "Even" if value % 2 == 0 else "Odd"
    print(f"The number {value} is :{message}")
