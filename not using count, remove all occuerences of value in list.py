list1= [10,20,30,10,20,30,20,40,30,20,50,30,20,10,10]
Value= 10

while True:
    if Value in list1:
        list1.remove(Value)
    else:
        break

print(list1)
