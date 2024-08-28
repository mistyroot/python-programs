list1=[]
n=int(input("Enter how many values?"))


for i in range(n):
    value=int(input("Enter value "))
    list1.append(value)

pos1=int(input("Pos1 :"))
pos2=int(input("Pos2 :"))

print(f'Before Swaping {list1}')

list1[pos1-1],list1[pos2-1]=list1[pos2-1],list1[pos1-1]

print(f'After Swaping {list1}')
