#nested while loop- armstrong between 100 and 999
num =100
while num<=999:
    num1=num
    s=0
    while num1>0:
        r=num1 % 10
        s=s+(r**3)
        num1=num1//10
    if s==num:
        print(num)
    num=num+1

    