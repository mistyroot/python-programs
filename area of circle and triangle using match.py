print("***MENU***")
print("1.Area of circle")
print("2.Area of Triangle")
print("3.Exit")

opt=int(input("Enter your option"))
match opt:
    case 1:
        r= float(input("Enter radius of circle"))
        a=3.14*r*r
        print(f"Area of circle is {a:.2f}")
    case 2:
        base= float(input("Enter base of triangle"))
        height=float(input("Enter height of triangle"))
        a= 0.5*base*height
        print(f"Area of triangle is {a:.2f}")
    case 3:
        print("Thanks for using menu")
    case _:
        print("please enter option between 1 3")
    