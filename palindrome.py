num=int(input("Enter any number"))
rev=0
num1=num
while num>0:
    r=num%10
    rev=(rev*10)+r
    num=num//10

print(num)
if rev==num1:
    print("Pal")
else:
    print("Not pal")