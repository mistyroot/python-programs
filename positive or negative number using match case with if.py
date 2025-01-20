num= int(input("Enter any number"))
match num:
    case num if num>0:
        print("positive number")
    case num if num<0:
        print("Negative number")
    case _:
        print("Zero")
