n= int(input("Enter how many values:"))

list1=[]

for i in range(n):
    value= int(input("Enter any value:"))
    list1.append(value)
print(f"List is {list1}")

list1.sort()

first_max= list1[-1]
c=0
for value in list1:
    if value== first_max:
        c=c+1
print(f"second maximum is {list1[-(c+1)]}")
