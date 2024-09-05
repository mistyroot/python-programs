stack=[]

while True:
    print("1. Push")
    print("2. Pop")
    print("3. View")
    print("4. Exit")
    opt = int(input("Enter your option:"))
    if opt == 1:
        value = int(input("Enter any value:"))
        stack.append(value)
        print("Value pushed inside stack")
    elif opt==2:
        if len(stack)==0:
            print("Stack is empty")
        else:
            value=stack.pop()
            print(f"Value pop from stack is {value}")
    elif opt==3:
        print(f"Stack is {stack}")
    elif opt==4:
        break
    else:
        print(f"Invalid option")
