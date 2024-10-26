list1= [10,20,30,40,50,10,20,30,40,50,90,80,80,70,90,50,30]

#remove duplicates
list2= []
for value in list1:
    if value not in list2:
        list2.append(value)

print(list1)
print(list2)

#read value from list2
for value in list2:
    c=0
    for x in list1:
        if value == x:
            c=c+1
    if c>1:
        print(value)

