matrix= [[1,2,3],[4,5,6],[7,8,9]]

print("Upper Triangle:")
for i in range(3):
    for j in range(3):
        if j >= i:
            print(matrix[i][j], end='')
        else:
            print(' ', end="")
    print()

print("Lower Triangle:")
for i in range(3):
    for j in range(3):
        if j<=i:
            print(matrix[i][j], end='')
        else:
            print(' ', end='')
    print()


