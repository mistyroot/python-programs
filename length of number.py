#length of number
num= int(input("Enter any number"))
c=0
while num>0:
    c=c+1
    num=num//10
print(f"length of digits is {c}")
