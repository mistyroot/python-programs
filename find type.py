#write a program to find input character is alphabet, digit or special character

ch=input("Enter single character")
if(ch>="A" and ch<="Z") or (ch>="a" and ch<="z"):
    print(f'{ch} is alphabet')
elif (ch>"0" and ch<"9"):
    print (f"{ch} is digit")
else:
    print(f"{ch} is special character")
