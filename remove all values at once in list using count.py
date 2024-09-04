list1 = [10,10,20,30,40,10,10,20,30,10]
Value= 10

c= list1.count(Value)
for i in range(c):
    list1.remove(Value)

print(list1)