list1=[3,9,12,56,23,98,45,12,6,8,9,3,5,12,15,76,34,12,67,87,98]

# count values which are >50
count=0
for value in list1:
    if value>50:
        print(value,end=' ')
        count=count+1

print(f'\nCount is {count}')

# count values in given range
start=int(input("Enter Start Value "))
end=int(input("Enter End Value "))
count=0
for value in list1:
    if value>=start and value<=end:
        print(value,end=' ')
        count=count+1
print(f'\nCount is {count}')

# count even numbers and odd numbers in list

ecount=0
ocount=0
for value in list1:
    if value%2==0:
        ecount+=1
    else:
        ocount+=1

print(f'Even Count {ecount}')
print(f'Odd Count {ocount}')
