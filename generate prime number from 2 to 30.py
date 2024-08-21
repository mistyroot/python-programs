for num in range(2,21):
    c=0
    i=1
    for i in range(i, num+1):
        if num%i==0:
            c+=1
    if c==2:
        print(num)