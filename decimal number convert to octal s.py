#input decimal number convert to octal string
num = int(input("Enter any decimal number: "))
octal = ''

while num != 0:
    r = num % 8
    octal = str(r) + octal
    num //= 8

print(f"Octal representation: {octal}")
