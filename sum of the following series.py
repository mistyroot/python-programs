#sum of the following series 1^1 + 2^2 + 3^3 + . . + n^n
n=int(input("Enter value of n"))
s=0
for i in range(1,n+1):
    s=s+(i**i)

print(f'sum of series is {s}')


