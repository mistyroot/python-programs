sub_1 = int(input("Enter the sub_1 marks out of 100: "))
sub_2 = int(input("Enter the sub_2 marks out of 100: "))

Total = sub_1 + sub_2
print("The total marks are: ", Total)

Average = (sub_1 + sub_2)/ 2
print("The Average marks are: ", Average)

percentage = Total / 200 * 100
print("The percentage is: ", percentage)

if percentage >= 90:
    print("The grade obtained is A:")
elif 90>= percentage >= 80:
    print("The Grade obtained is B+:")
elif 80>= percentage >= 70:
    print("The Grade obtained is B:")
elif 70>= percentage >= 60:
    print("The Grade obtained is C:")
elif percentage <= 60:
    print("The Grade obtained is Fail:")