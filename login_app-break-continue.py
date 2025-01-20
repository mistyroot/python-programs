valid=False
for i in range(3):
    uname=input("username:")
    pwd=input("Password:")
    if uname=="nit" and pwd=="n123":
        valid=True
        break
if valid:
    print("Welcome")
else:
    print("3 attept are completed, your account is blocked")
