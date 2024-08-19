#Number of 1 Bits
# Write a program that takes the binary representation of a positive integer and returns the number of 
# set bits it has (also known as the Hamming weight).
# Input: n = 11
# Output: 3
# Explanation:

# The input binary string 1011 has a total of three set bits.


num=int(input("Enter any number "))
c=0
while num>0:
    b=num%2
    if b==1:
        c=c+1
    num=num//2

print(c)
