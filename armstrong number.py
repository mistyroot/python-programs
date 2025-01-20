#armstrong number  153= 1^3 + 5^3 + 3^3  = 153

#logic for 3 digit number
num=int(input("Enter any number between 100 to 999"))
num1=num
s=0
while num>0:
    d=num%10
    s=s+(d**3)
    num=num//10

if num1==s:
    print("armstrong number")
else:
    print("not armstrong number")
