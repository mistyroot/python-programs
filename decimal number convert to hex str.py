#input decimal number convert to hex string
num = int(input("Enter any decimal number: "))
hexadecimal = ''

while num != 0:
    r = num % 16
    if r < 10:
        hexadecimal = str(r) + hexadecimal
    else:
        hexadecimal = chr(ord('A') + r - 10) + hexadecimal
    num //= 16

print(f"Hexadecimal representation: {hexadecimal}")

