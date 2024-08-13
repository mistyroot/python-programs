a=4
match a:
    case 1|3:
        print("1 or 3")
    case 5|7|12:
        print("5 or 7 or 12")
    case 4|8|16:
        print("4 or 8 or 16")
    case _:
        print("does not match any pattern")