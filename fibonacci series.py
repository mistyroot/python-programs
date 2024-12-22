#fibonacci series
#factorial 0 1 1 2 3 5 8 13

n=int(input("Enter how many terms?"))
a=0
b=1
print(a,b,end=' ')
for i in range(n-2):
    c=a+b
    print(c,end=' ')
    a=b
    b=c

