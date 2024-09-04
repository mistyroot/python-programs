list1= [10,23,21,35,32,67,54,86,35,89,43,54,20]
value= 54

#before remove
print(list1)

l= len(list1)
index = 0

while index< l:
    if list1[index] == value:
        del list1[index]
        l= l-1
        continue
    else:
        index = index + 1
#after remove 
print(list1)

