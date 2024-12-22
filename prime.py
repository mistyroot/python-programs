num=int(input("Enter any number "))
c=0
i=1

while i<=num:
    r=num%i
    if r==0:
      c=c+1
    i=i+1

if c==2:
    print(f'{num} is prime')
else:
    print(f'{num} is not prime')


