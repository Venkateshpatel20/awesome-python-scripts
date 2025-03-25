def calculator():
    
    while True:
        print('"""""""Calculator"""""""')
        a = float(input("enter a value:"))
        b = float(input("enter b value:"))
        print("choose the")

        print("Enter 1 for Addition")
        print("Enter 2 for Substraction")
        print("Enter 3 for Multiplication")
        print("Enter 4 for Division")
        print("Enter 5 for Floor operation")
        print("Enter 6 for Modulo")
        print("Enter 7 for Power operation")
        #print("Choose the operation to be performed:")
        c = int(input("choose the operation to perform:"))
        # x = bool(True)
        while True:
            if c==1:
                print("value of a \"+\" b:",a+b)
            elif c == 2:
                print(f"value of {a} - {b} = ",a-b)
            elif c == 3:
                print(f"value of {a} X {b} = ",a*b)
            elif c == 4:
                print(f"value of {a} / {b} = ",a/b)
            elif c == 5:
                print(f"value of {a} // {b} = ",a//b)
            elif c == 6:
                print(f"value of {a} % {b} = ",a%b) 
            elif c == 7:
                print(f"value of {a} ** {b} = ",a**b)   
            else :
                print("invalid entry")
        x = bool(input("do you want to continue(yse:1 or no:0)"))
