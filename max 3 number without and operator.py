a=int(input("Enter value of a"))
b=int(input("Enter value of b"))
c=int(input("enter value of c"))
if a>b:
    if a>c:
        print(f"{a} is max")
    else:
        print(f"{c} is max")
elif b>a:
    if b>c:
        print(f"{b} is max")
    else:
        print(f"{c} is max")
elif c>a:
    if c>b:
        print(f"{c} is max")
    else:
        print(f"{b} is max")
else:
    print("equal")
