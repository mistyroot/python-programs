list1=[1,5,9,2,6,7,8,12,17,23,65,87,45,23,89,87,69,54,34,23,13,89]

even_count=0
odd_count=0

for i in range(len(list1)):
    if list1[i]%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1

print(f'List is {list1}')
print(f'Even Count {even_count}')
print(f'Odd Count {odd_count}')


