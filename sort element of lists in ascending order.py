n= int(input("Enter how many values:"))
list1=[]
for i in range(n):
    value=int(input("Enter any value:"))
    list1.append(value)
print(f"Before sorting:{list1}")

for i in range(n):
    for j in range(n-1):
        if list1[j]> list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]

print(f"After sorting: {list1}")
