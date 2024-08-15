#input decimal number convert to binary string
num=int(input("Enter any number"))
binary=''
while num!=0 and num!=1:
    r=num%2
    binary=binary+str(r)
    num=num//2
binary=binary+str(num)
print(binary[::-1])