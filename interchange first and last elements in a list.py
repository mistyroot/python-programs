list1=[10,20,30,40,50]
print(f'Before swaping {list1}')

temp=list1[0]
list1[0]=list1[-1]
list1[-1]=temp

print(f'After swaping {list1}')

list1[0],list1[-1]=list1[-1],list1[0]
print(f'After swaping {list1}')
