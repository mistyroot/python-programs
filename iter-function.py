list1=list(range(10,110,10))
print(list1)

a=iter(list1)
value1=next(a)
value2=next(a)
value3=next(a)
print(value1,value2,value3)

for value in a:
    print(value)

