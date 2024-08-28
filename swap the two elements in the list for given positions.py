# Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90]

# Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
# Output : [1, 5, 3, 4, 2]'''


list1=[23, 65, 19, 90]
pos1=1
pos2=3
print(f'Before swaping {list1}')

list1[pos1-1],list1[pos2-1]=list1[pos2-1],list1[pos1-1]
print(f'After swaping {list1}')
