num=int(input("Enter any number"))

fact=1
for i in range(1,num+1):
    fact=fact*i
else:
    print(f'factorial of {num} is {fact}')


fact=1
i=1
while i<=num:
    fact=fact*i
    i=i+1
else:
    print(f'factorial of {num} is {fact}')
