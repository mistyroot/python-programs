list1=[5,2,3,-1,4,-4,-6,0,0,-12,-25,-9,3,6,7,0,0,12,56,-34,0,0]

pcount=0

for i in range(len(list1)): # 0 1 2 3 4 5 6 7
    num=list1[i]
    c=0
    for j in range(1,num+1):
        if num%j==0:
            c=c+1
    if c==2:
        print(num)
