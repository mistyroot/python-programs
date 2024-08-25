#       *  
#      * * 
#     *   *
#    *     *
#   *       *

space=4
for i in range (1,6):
    for s in range (space):
        print(" ", end='')
    for j in range(1,i+1):
        print("*", end='')
    print()
    space=space-1

space=0

for i in range(5,0,-1):
    for s in range(space):
        print(" ", end='')
    for j in range(1,i+1):
        print("*", end='')
    print()
    space=space+1


