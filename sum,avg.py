#sum,avg
n=int(input("Enter value of n"))

s=0
for i in range(n): # start=0,stop=n,step=1
    num=int(input("Enter any number "))
    s=s+num

print(f'Sum is {s}')
print(f'Avg is {s/n:.2f}')


