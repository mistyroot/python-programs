print("Enter elements of matrix1")
matrix1=[[int(input()) for j in range(3)] for i in range(3)]
print("Enter elements of matrix2")
matrix2=[[int(input()) for j in range(3)] for i in range(3)]
matrix3=[[matrix1[i][j]+matrix2[i][j] for j in range(3)] for i in range(3)]

print(matrix1)
print(matrix2)
print(matrix3)

# without comprehension
# matrix1=[]
# for i in range(3):
#     row=[]
#     for j in range(3):
#         value=int(input("Enter value "))
#         row.append(value)
#     matrix1.append(row)

# print(matrix1)
