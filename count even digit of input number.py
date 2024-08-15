#count even digit of input number
num=int(input("Enter any number"))
c=0
while num>0:
    r=num%10
    if r%2==0:
        c=c+1
    num=num//10

print(f"count of even digit is {c}")