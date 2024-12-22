# if n is odd, print weird
# if n is even and inclusive range of 2 and 5, print not weird
# if n is even and inclusive range of 6 and 20, print weird
# if n is even and greater than 20, print not weird

n=int(input("number"))
if n%21 !=0:
    print("weird")
elif n>=2 and n<=5:
    print("Not weird")
elif n>6 and n<=20:
    print("weird")
elif n>20:
    print("Not weird")


