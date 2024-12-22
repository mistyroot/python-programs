# A= a b c
#    d e f

# A transpose= a d
#              b e
#              c f

matrix=[[1,2,3],[4,5,6],[7,8,9]]

print("Original Matrix")
for i in range(3):
    for j in range(3):
        print(matrix[i][j],end=' ')
    print()

print("Matrix Transpose")
for i in range(3):
    for j in range(3):
        print(matrix[j][i],end=' ')
    print()

