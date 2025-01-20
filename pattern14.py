# 12345
#  2345
#   345
#    45
#     5


for i in range(1,6):
    for j in range(1,6):
        if j >=i:
            print(j, end='')
        else:
            print(' ', end='')
    print()
