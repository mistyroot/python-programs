# input format
# first line contain no. of values
# second line contain values
# output
# print median

n= int(input("Enter the number of values: "))

list1= list(map(int,input("Enter the values: ").split()))
if n%2!=0:
    m=n//2
    print(list1[m])

else:
    m=n//2
    value1= list1[m]
    value2= list1[m-1]
    print((value1+value2)/2)
