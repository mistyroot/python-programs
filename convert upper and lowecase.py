#convert upper and lowecase
#here use chr() which is used convert character value from ascii value
#here use ord() which is used convert ascii value from character value

ch=input("Enter alphabet")
if ch>="a" and ch <="z":
    print(f"Uppercase {chr(ord(ch)-32)}")
elif ch>="A" and ch<= "Z":
    print(f"Lowercase {chr(ord(ch)+32)}")
else:
    print(f"character is not alphabet")
