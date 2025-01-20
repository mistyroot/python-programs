num=int(input("Enter any number"))
i=1
c=0
while i<=num:
    if num%i==0:
        c=c+1
    if c>2:
        break
    i=i+1

if c==2:
    print(f'{num} is prime')
else:
    print(f'{num} is not prime')
