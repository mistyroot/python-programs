# list1= [10,20,30,40,50,10,20,30,40,50,90,80,80,70]
# list2= []

# for value in list1:
#     if value not in list2:
#         list2.append(value)

# print(list1)
# print(list2)


#convert to set and then print list, set will remove duplicates
list1= [10,20,30,40,50,10,20,30,40,50,90,80,80,70]
list2= list(set(list1))
print(list1)
print(list2)
