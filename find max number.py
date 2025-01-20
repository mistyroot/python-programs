a=int(input("Enter a 1st integer value:"))
b=int(input("Enter a 2nd integer value:"))
c=int(input("Enter a 3rd integer value:"))
res= a if a>b and a>c else b if b>=a and b>=c else c
print(f"max of {a},{b},{c} is {res}")
