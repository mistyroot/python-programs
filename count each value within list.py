list1 = [1,2,3,2,4,5,5,76,5,4,3,4,5,6,8,7,8,7,5,3,2,2]
list2= []

for value in list1:
    if value not in list2:
        list2.append(value)
print(list1)
print(list2)

for value in list2:
    c= list1.count(value)
    print(f"{value}--------> {c}")

    