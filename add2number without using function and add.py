# Function to add two numbers using bitwise operations
def add(a, b):
    while b != 0:
        # Carry now contains common set bits of a and b
        carry = a & b
        
        # Sum of bits of a and b where at least one of the bits is not set
        a = a ^ b
        
        # Carry is shifted by one so that adding it to a gives the required sum
        b = carry << 1
    
    return a

# Input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate the sum
result = add(num1, num2)

# Display the result
print(f"The sum of {num1} and {num2} is {result}")

