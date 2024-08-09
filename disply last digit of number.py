#any number%10 display last digit
num = int(input("Enter a number"))
last_digit = num % 10
if last_digit % 3 == 0:
    print(f"{num} last digit is divisible by 3")
else:
    print(f"{num} last digit is not divisible by 3")
