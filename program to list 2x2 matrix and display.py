matrix=[]
for i in range(2):
    row=[]
    for j in range(2):
        value= int(input("Enter any value:"))
        row.append(value)
    matrix.append(row)

print(matrix)

for row in matrix:
    for value in row:
        print(value, end=' ')
    print()
