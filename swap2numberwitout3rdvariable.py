
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

# Swap using XOR
a = a ^ b
b = a ^ b
a = a ^ b

#x,y=y,x
#print(x,y)

print(f"After swapping: a = {a}, b = {b}")

# example with actual numbers:
# Suppose a = 5 (binary 0101) and b = 3 (binary 0011).
# a = a ^ b:
# a = 0101 ^ 0011 = 0110 (binary for 6)
# b = a ^ b:
# b = 0110 ^ 0011 = 0101 (binary for 5, original value of a)
# a = a ^ b:
# a = 0110 ^ 0101 = 0011 (binary for 3, original value of b)
# After these operations, a is 3 and b is 5, effectively swapping their values.

