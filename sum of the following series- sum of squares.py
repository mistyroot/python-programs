
# Wrie a program to find the sum of the following series 1^2 + 2^2 + 3^2 + . . +n^2
n=int(input("Enter value of n"))
s=0
for i in range(1,n+1):
    s=s+(i**2)

print(f'sum of series is {s}')
    


