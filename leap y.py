#leap or not witout using and operator
year=int(input("Enter year"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"{year} is leap year")
        else:
            print("Not a leap year")
    else:
        print("leap year")
else:
    print("Not a leap year")

