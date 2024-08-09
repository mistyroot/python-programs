age= int(input("Enter age:"))
name=input("Enter name:")


if age>=18:
    print(f"{name} is eligible for vote")
else:
    print(f"{name} is not eligible for vote")

print("thanks for using voter eligibility app")