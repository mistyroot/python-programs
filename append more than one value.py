list1=[10,20,30]
print(f'Before append list is {list1}')
list1[len(list1):]=[40,50,60]
print(f'After append list is {list1}')
list1[len(list1):]=range(70,110,10)
print(f'After append list is {list1}')
list1[len(list1):]="NIT"
print(f'After append list is {list1}')

sales1=[1000,2000,3000,4000]
sales2=[5000,7000,9000,10000,56000]
print(sales1)
sales1[len(sales1):]=sales2
print(sales1)
