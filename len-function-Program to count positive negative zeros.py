list1=[1,2,3,-1,4,-4,-6,0,0,-12,-25,-9,3,6,7,0,0,12,56,-34,0,0]

pcount=0
ncount=0
zcount=0

for i in range(len(list1)):
    if list1[i]>0:
        pcount+=1
    elif list1[i]<0:
        ncount+=1
    else:
        zcount+=1

print(f'list is {list1}')
print(f'+ve Count {pcount}')
print(f'-ve Count {ncount}')
print(f'zero count {zcount}')
