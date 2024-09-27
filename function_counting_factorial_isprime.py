def count_digits(num):
    c=0
    while num>0:
        c=c+1
        num= num//10
    print(f"Count of digits {c}")
    
def isprime(num):
    c=0
    for i in range(1, num + 1):
        if num% i==0:
            c=c+1
    if c==2:
        print("Prime")
    else:
        print("Not prime")

def factorial(num1):
    fact=1
    for i in range(1, num1 + 1):
        fact=fact*i
    print(f"factorial is {fact}")

count_digits(4567)
isprime(6)
isprime(7)
factorial(4)
