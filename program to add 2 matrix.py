matrix1=[]
matrix2=[]
matrix3=[]

print("Enter elements of matrix1")
for i in range(2):
    row=[]
    for j in range(2):
        value=int(input("Enter any value "))
        row.append(value)
    matrix1.append(row)

print("Enter elements of matrix2")
for i in range(2):
    row=[]
    for j in range(2):
        value=int(input("Enter any value "))
        row.append(value)
    matrix2.append(row)

for i in range(2):
    row=[]
    for j in range(2):
        row.append(matrix1[i][j]+matrix2[i][j])
    matrix3.append(row)

print(matrix1)
print(matrix2)
print(matrix3)
