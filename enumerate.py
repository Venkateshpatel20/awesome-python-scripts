#syntax enumerate(iterable,start=0)
def enumerate_exmpl():
    """Demonstrate the use of enumerate function in Python"""
    my_list = ["A","B","C","D"]
    #Using enumerate without a starting index
    print("with default  index[0]")
    for index,item in enumerate(my_list):
        print(f"index: {index},item: {item}")

    print("specifying a starting index(1)")
    for index, item in enumerate(my_list,1):
        print(f"index: {index} , item {item}")
    
    print("Enumerating a string without specific index specification ")
    my_string = "my string"
    print("enumerating a string")
    for index,item in enumerate(my_string):
        print(f"character:{item} for index:{index}")
    print("enumerating a string")
    for index,chr in enumerate(my_string,2):
        print(f"character:{chr} for index: {index}")
    
    print("enumerating a tuple with default index")
    my_tuple = (10,20,30)
    for index,value in enumerate(my_tuple):
        print(f"index {index} holds item {value}")
    print("enumerating a tuple with specific index")
    for index,item in enumerate(my_tuple,3):
        print(f"index {index} holds item {item}")
    
    print("Enumerating a with list comphrehension")
    indexed_list = [(index, item.upper()) for index,item in enumerate(my_list)]
    print(f"Indexed List:{indexed_list}")

if __name__ == "__main__":
    enumerate_exmpl()